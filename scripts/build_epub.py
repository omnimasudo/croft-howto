#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["ebooklib", "markdown", "beautifulsoup4", "httpx", "pillow"]
# ///
"""
Build an EPUB from the Claude How-To markdown files.

Usage:
    Run from the repository root directory:
        ./scripts/build_epub.py

    Or run directly with Python/uv:
        uv run scripts/build_epub.py
        python scripts/build_epub.py

    The script uses inline script dependencies (PEP 723), so uv will
    automatically install required packages in an isolated environment.

Output:
    Creates 'claude-howto-guide.epub' in the repository root directory.

Features:
    - Organizes chapters by folder structure (01-slash-commands, etc.)
    - Renders Mermaid diagrams as PNG images via Kroki.io API
    - Generates a cover image from the project logo
    - Converts internal markdown links to EPUB chapter references
    - Handles SVG images by replacing with alt text (unsupported in EPUB)

Requirements:
    - uv (recommended) or Python 3.10+ with dependencies installed
    - Internet connection for Mermaid diagram rendering
    - Repository structure with markdown files and claude-howto-logo.png
"""

import base64
import re
import zlib
from pathlib import Path
import httpx
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from ebooklib import epub
import markdown
from bs4 import BeautifulSoup


# Cache for mermaid images to avoid re-fetching (stores (image_data, filename) tuples)
_mermaid_cache: dict[str, tuple[bytes, str]] = {}
_mermaid_counter = 0

# Track which mermaid images have been added to the book
_mermaid_added_to_book: set[str] = set()

# Mapping from source paths to EPUB chapter filenames
_path_to_chapter: dict[str, str] = {}


def mermaid_to_image(mermaid_code: str) -> tuple[bytes, str] | None:
    """Convert mermaid code to PNG image using Kroki.io API."""
    global _mermaid_counter

    # Check cache - return cached image data and filename to avoid duplicates
    cache_key = mermaid_code.strip()
    if cache_key in _mermaid_cache:
        return _mermaid_cache[cache_key]

    try:
        # Use Kroki.io API - accepts deflate-compressed, base64-encoded diagrams
        compressed = zlib.compress(mermaid_code.encode('utf-8'), level=9)
        encoded = base64.urlsafe_b64encode(compressed).decode('ascii')
        url = f"https://kroki.io/mermaid/png/{encoded}"

        response = httpx.get(url, timeout=30, follow_redirects=True)
        if response.status_code == 200:
            _mermaid_counter += 1
            img_data = response.content
            img_name = f"mermaid_{_mermaid_counter}.png"
            _mermaid_cache[cache_key] = (img_data, img_name)
            return img_data, img_name
        else:
            print(f"  Warning: Kroki API returned {response.status_code}")
            return None
    except Exception as e:
        print(f"  Warning: Failed to render mermaid diagram: {e}")
        return None


def sanitize_mermaid(mermaid_code: str) -> str:
    """Sanitize mermaid code to avoid markdown parsing issues.

    Mermaid's markdown-in-nodes feature incorrectly interprets numbered
    lists (e.g., "1. Item") inside node labels. This escapes the period
    to prevent that.
    """
    # Escape numbered list patterns inside brackets: [1. Text] -> [1\. Text]
    # Match patterns like [1. or ["1. inside node definitions
    sanitized = re.sub(r'\[(["\']?)(\d+)\.(\s)', r'[\1\2\\.\3', mermaid_code)
    return sanitized


def process_mermaid_blocks(md_content: str, book: epub.EpubBook) -> str:
    """Find mermaid code blocks and replace with image references."""
    # Pattern to match ```mermaid ... ```
    pattern = r'```mermaid\n(.*?)```'

    def replace_mermaid(match):
        mermaid_code = sanitize_mermaid(match.group(1))
        result = mermaid_to_image(mermaid_code)
        if result:
            img_data, img_name = result
            # Only add image to book if not already added
            if img_name not in _mermaid_added_to_book:
                img_item = epub.EpubItem(
                    uid=img_name.replace('.', '_'),
                    file_name=f"images/{img_name}",
                    media_type="image/png",
                    content=img_data
                )
                book.add_item(img_item)
                _mermaid_added_to_book.add(img_name)
            # Return markdown image reference
            return f'\n![Diagram](images/{img_name})\n'
        else:
            # Fallback: show as code block with a note
            return f'\n**[Diagram]**\n```\n{mermaid_code}```\n'

    return re.sub(pattern, replace_mermaid, md_content, flags=re.DOTALL)


def create_cover_image(logo_path: Path, title: str = "Claude Code\nHow-To Guide") -> bytes:
    """Create a cover image by composing the logo with title text on top.

    Args:
        logo_path: Path to the PNG logo file
        title: Title text to overlay on the cover

    Returns:
        PNG image data as bytes
    """
    # Target cover dimensions (standard ebook cover ratio ~1.6:1 height:width)
    cover_width = 600
    cover_height = 900

    # Background color matching the logo gradient
    bg_color = (26, 26, 46)  # #1a1a2e from the logo

    # Create the cover canvas
    cover = Image.new('RGB', (cover_width, cover_height), bg_color)
    draw = ImageDraw.Draw(cover)

    # Load and scale the logo
    with Image.open(logo_path) as logo:
        # Scale logo to fit cover width with some padding
        target_width = cover_width - 60  # 30px padding on each side
        scale_factor = target_width / logo.width
        new_height = int(logo.height * scale_factor)
        logo_scaled = logo.resize((target_width, new_height), Image.Resampling.LANCZOS)

        # Handle transparency
        if logo_scaled.mode == 'RGBA':
            # Composite onto a background matching cover color
            logo_bg = Image.new('RGB', logo_scaled.size, bg_color)
            logo_bg.paste(logo_scaled, mask=logo_scaled.split()[3])
            logo_scaled = logo_bg
        elif logo_scaled.mode != 'RGB':
            logo_scaled = logo_scaled.convert('RGB')

        # Position the logo in the lower portion of the cover
        logo_x = (cover_width - logo_scaled.width) // 2
        logo_y = cover_height - logo_scaled.height - 80  # 80px from bottom
        cover.paste(logo_scaled, (logo_x, logo_y))

    # Add title text at the top
    # Try to use a nice font, fall back to default
    font_size = 72
    font = ImageFont.load_default()
    try:
        # Try common system fonts on macOS
        for font_name in [
            '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
            '/System/Library/Fonts/Helvetica.ttc',
            'Arial Bold',
            'Helvetica Bold',
        ]:
            try:
                font = ImageFont.truetype(font_name, font_size)
                break
            except OSError:
                continue
    except Exception:
        pass

    # Draw title text (centered, near top)
    title_color = (78, 205, 196)  # #4ecdc4 - teal from the logo gradient

    # Split title into lines and draw each centered
    lines = title.split('\n')
    y_offset = 120
    line_spacing = 90

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x = (cover_width - text_width) // 2
        draw.text((x, y_offset), line, font=font, fill=title_color)
        y_offset += line_spacing

    # Add a subtle subtitle
    subtitle = "Complete Guide to Claude Code Features"
    subtitle_font_size = 24
    subtitle_font = ImageFont.load_default()
    try:
        for font_name in [
            '/System/Library/Fonts/Supplemental/Arial.ttf',
            '/System/Library/Fonts/Helvetica.ttc',
            'Arial',
            'Helvetica',
        ]:
            try:
                subtitle_font = ImageFont.truetype(font_name, subtitle_font_size)
                break
            except OSError:
                continue
    except Exception:
        pass

    subtitle_color = (168, 178, 209)  # #a8b2d1 - light gray from logo
    bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = bbox[2] - bbox[0]
    subtitle_x = (cover_width - subtitle_width) // 2
    subtitle_y = y_offset + 20
    draw.text((subtitle_x, subtitle_y), subtitle, font=subtitle_font, fill=subtitle_color)

    # Save to bytes
    buffer = BytesIO()
    cover.save(buffer, format='PNG', optimize=True)
    return buffer.getvalue()


def get_chapter_order():
    """Define the order of chapters based on folder structure."""
    return [
        ("README.md", "Introduction"),
        ("LEARNING-ROADMAP.md", "Learning Roadmap"),
        ("QUICK_REFERENCE.md", "Quick Reference"),
        ("claude_concepts_guide.md", "Claude Concepts Guide"),
        ("01-slash-commands", "Slash Commands"),
        ("02-memory", "Memory"),
        ("03-skills", "Skills"),
        ("04-subagents", "Subagents"),
        ("05-mcp", "MCP Protocol"),
        ("06-hooks", "Hooks"),
        ("07-plugins", "Plugins"),
        ("08-checkpoints", "Checkpoints"),
        ("09-advanced-features", "Advanced Features"),
        ("resources.md", "Resources"),
    ]


def convert_internal_links(html: str, current_file: Path, root_path: Path) -> str:
    """Convert markdown links to internal EPUB chapter links."""
    soup = BeautifulSoup(html, 'html.parser')

    for link in soup.find_all('a'):
        href = link.get('href', '')
        if not href or href.startswith(('http://', 'https://', 'mailto:', '#')):
            continue

        # Remove anchor part for path resolution
        anchor = ''
        if '#' in href:
            href, anchor = href.split('#', 1)
            anchor = '#' + anchor

        # Resolve relative path from current file's directory
        if href:
            resolved = (current_file.parent / href).resolve()
            try:
                rel_to_root = resolved.relative_to(root_path)
            except ValueError:
                # Link points outside the repo
                continue

            # Normalize the path for lookup
            lookup_path = str(rel_to_root)

            # Try various path forms for matching
            paths_to_try = [
                lookup_path,
                lookup_path.rstrip('/'),
                lookup_path + '/README.md' if not lookup_path.endswith('.md') else lookup_path,
            ]

            for path in paths_to_try:
                if path in _path_to_chapter:
                    link['href'] = _path_to_chapter[path] + anchor
                    break

    return str(soup)


def md_to_html(md_content: str, current_file: Path, root_path: Path, book: epub.EpubBook) -> str:
    """Convert markdown to HTML with proper styling.

    Handles:
    - Mermaid diagrams (rendered as PNG images)
    - SVG images (replaced with alt text)
    - Internal links (converted to EPUB chapter references)
    - Standard markdown features
    """
    # Process mermaid blocks first (before markdown conversion)
    md_content = process_mermaid_blocks(md_content, book)

    # Convert markdown to HTML
    html = markdown.markdown(
        md_content,
        extensions=[
            'tables',
            'fenced_code',
            'codehilite',
            'toc',
        ]
    )

    # Clean up any SVG references (they won't work in EPUB)
    soup = BeautifulSoup(html, 'html.parser')
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if src.endswith('.svg'):
            # Replace SVG with alt text
            alt = img.get('alt', 'Image')
            img.replace_with(f'[{alt}]')

    html = str(soup)

    # Convert internal links to EPUB chapter references
    html = convert_internal_links(html, current_file, root_path)

    return html


def collect_folder_files(folder_path: Path) -> list[tuple[Path, str]]:
    """Collect all markdown files from a folder, README first."""
    files = []

    # Get README first if it exists
    readme = folder_path / "README.md"
    if readme.exists():
        files.append((readme, "Overview"))

    # Get all other markdown files
    for md_file in sorted(folder_path.glob("*.md")):
        if md_file.name != "README.md":
            title = md_file.stem.replace("-", " ").replace("_", " ").title()
            files.append((md_file, title))

    # Recursively get subfolders
    for subfolder in sorted(folder_path.iterdir()):
        if subfolder.is_dir() and not subfolder.name.startswith('.'):
            subfiles = collect_folder_files(subfolder)
            for sf, st in subfiles:
                # Prefix with subfolder name
                rel_path = sf.relative_to(folder_path)
                if len(rel_path.parts) > 1:
                    prefix = rel_path.parts[0].replace("-", " ").replace("_", " ").title()
                    files.append((sf, f"{prefix}: {st}"))
                else:
                    files.append((sf, st))

    return files


def create_epub(root_path: Path, output_path: Path):
    """Create the EPUB from markdown files."""
    book = epub.EpubBook()

    # Set metadata
    book.set_identifier('claude-howto-guide')
    book.set_title('Claude Code How-To Guide')
    book.set_language('en')
    book.add_author('Claude Code Community')

    # Add cover image from PNG logo
    logo_path = root_path / "claude-howto-logo.png"
    if logo_path.exists():
        print("Adding cover image...")
        cover_data = create_cover_image(logo_path)
        book.set_cover("cover.png", cover_data)

    # Add CSS
    style = '''
    body { font-family: Georgia, serif; line-height: 1.6; padding: 1em; }
    h1 { color: #333; border-bottom: 2px solid #e67e22; padding-bottom: 0.3em; }
    h2 { color: #444; margin-top: 1.5em; }
    h3 { color: #555; }
    code { background: #f4f4f4; padding: 0.2em 0.4em; border-radius: 3px; font-family: monospace; }
    pre { background: #f4f4f4; padding: 1em; overflow-x: auto; border-radius: 5px; }
    pre code { background: none; padding: 0; }
    table { border-collapse: collapse; width: 100%; margin: 1em 0; }
    th, td { border: 1px solid #ddd; padding: 0.5em; text-align: left; }
    th { background: #f4f4f4; }
    blockquote { border-left: 4px solid #e67e22; margin: 1em 0; padding-left: 1em; color: #666; }
    a { color: #e67e22; }
    img { max-width: 100%; height: auto; display: block; margin: 1em auto; }
    .diagram { text-align: center; margin: 1.5em 0; }
    '''
    nav_css = epub.EpubItem(
        uid="style_nav",
        file_name="style/nav.css",
        media_type="text/css",
        content=style
    )
    book.add_item(nav_css)

    chapters = []
    toc = []
    chapter_order = get_chapter_order()

    # First pass: build path-to-chapter mapping
    chapter_num = 0
    print("Building chapter mapping...")
    for item, display_name in chapter_order:
        item_path = root_path / item

        if item_path.is_file() and item_path.suffix == '.md':
            chapter_num += 1
            chapter_file = f'chap_{chapter_num:02d}.xhtml'
            _path_to_chapter[item] = chapter_file

        elif item_path.is_dir():
            folder_files = collect_folder_files(item_path)
            if not folder_files:
                continue

            chapter_num += 1
            # Map folder itself to first file (README)
            _path_to_chapter[item] = f'chap_{chapter_num:02d}_00.xhtml'
            _path_to_chapter[item.rstrip('/')] = f'chap_{chapter_num:02d}_00.xhtml'

            for i, (file_path, _) in enumerate(folder_files):
                rel_path = str(file_path.relative_to(root_path))
                _path_to_chapter[rel_path] = f'chap_{chapter_num:02d}_{i:02d}.xhtml'

    # Second pass: generate chapters with link conversion
    chapter_num = 0
    for item, display_name in chapter_order:
        item_path = root_path / item

        if item_path.is_file() and item_path.suffix == '.md':
            # Single file chapter
            chapter_num += 1
            content = item_path.read_text(encoding='utf-8')
            print(f"Processing: {item_path.name}")
            html_content = md_to_html(content, item_path, root_path, book)

            chapter = epub.EpubHtml(
                title=display_name,
                file_name=f'chap_{chapter_num:02d}.xhtml',
                lang='en'
            )
            chapter.content = f'''
            <html>
            <head><title>{display_name}</title></head>
            <body>
            <h1>{display_name}</h1>
            {html_content}
            </body>
            </html>
            '''
            chapter.add_item(nav_css)
            book.add_item(chapter)
            chapters.append(chapter)
            toc.append(chapter)

        elif item_path.is_dir():
            # Folder chapter with sub-sections
            folder_files = collect_folder_files(item_path)

            if not folder_files:
                continue

            chapter_num += 1
            sub_chapters = []

            for i, (file_path, file_title) in enumerate(folder_files):
                content = file_path.read_text(encoding='utf-8')
                print(f"Processing: {file_path.relative_to(root_path)}")
                html_content = md_to_html(content, file_path, root_path, book)

                sub_chapter = epub.EpubHtml(
                    title=file_title,
                    file_name=f'chap_{chapter_num:02d}_{i:02d}.xhtml',
                    lang='en'
                )

                if i == 0:
                    # First file gets the chapter title
                    sub_chapter.content = f'''
                    <html>
                    <head><title>{display_name}</title></head>
                    <body>
                    <h1>{display_name}</h1>
                    {html_content}
                    </body>
                    </html>
                    '''
                else:
                    sub_chapter.content = f'''
                    <html>
                    <head><title>{file_title}</title></head>
                    <body>
                    <h2>{file_title}</h2>
                    {html_content}
                    </body>
                    </html>
                    '''

                sub_chapter.add_item(nav_css)
                book.add_item(sub_chapter)
                chapters.append(sub_chapter)
                sub_chapters.append(sub_chapter)

            # Add folder as section with sub-chapters
            if sub_chapters:
                toc.append((epub.Section(display_name), sub_chapters))

    # Set table of contents
    book.toc = toc

    # Add navigation files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Set spine
    book.spine = ['nav'] + chapters

    # Write the EPUB
    epub.write_epub(str(output_path), book, {})
    print(f"EPUB created: {output_path}")


if __name__ == '__main__':
    root = Path(__file__).parent
    output = root / "claude-howto-guide.epub"
    create_epub(root, output)
