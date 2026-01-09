# Quick Start - Brand Assets

## Copy Assets to Your Project

```bash
# Copy all resources to your web project
cp -r resources/ /path/to/your/website/

# Or just the favicons for web
cp resources/favicons/* /path/to/your/website/public/
```

## Add to HTML (Copy & Paste)

```html
<!-- Favicons -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
<meta name="theme-color" content="#0d1f0d">
```

## Use in Markdown/Documentation

```markdown
# Claude How To

![Claude How To Logo](resources/logos/claude-howto-logo.svg)

![Icon](resources/icons/claude-howto-icon.svg)
```

## Recommended Sizes

| Purpose | Size | File |
|---------|------|------|
| Website header | 800×200 | `logos/claude-howto-logo.svg` |
| App icon | 256×256 | `icons/claude-howto-icon.svg` |
| Browser tab | 32×32 | `favicons/favicon-32.svg` |
| Mobile home screen | 128×128 | `favicons/favicon-128.svg` |
| Desktop app | 256×256 | `favicons/favicon-256.svg` |
| Small avatar | 64×64 | `favicons/favicon-64.svg` |

## Color Values

```css
/* Use these in your CSS */
--color-bg-dark: #0d1f0d;
--color-emerald: #10b981;
--color-emerald-dark: #059669;
--color-emerald-forest: #047857;
--color-mint: #6ee7b7;
--color-mint-light: #34d399;
```

## Icon Design Meaning

**Ascending Hexagons Represent**:
- 🟢 Bottom (Dark Emerald) = Beginner (Levels 1-3)
- 🟢 Middle (Bright Emerald) = Intermediate (Levels 4-6)
- 🟢 Top (Mint) = Advanced (Levels 7-10)

This symbolizes the learning progression from basics to mastery.

## What to Use Where

### Website
- **Header**: Logo (`logos/claude-howto-logo.svg`)
- **Favicon**: 32-bit (`favicons/favicon-32.svg`)
- **Social preview**: Icon (`icons/claude-howto-icon.svg`)

### GitHub
- **README badge**: Icon (`icons/claude-howto-icon.svg`) at 64-128px
- **Repository avatar**: Icon (`icons/claude-howto-icon.svg`)

### Social Media
- **Profile picture**: Icon (`icons/claude-howto-icon.svg`)
- **Banner**: Logo (`logos/claude-howto-logo.svg`)
- **Thumbnail**: Icon at 256×256px

### Documentation
- **Chapter headers**: Logo or icon (scaled to fit)
- **Navigation icons**: Favicon (32-64px)

---

See [README.md](README.md) for complete documentation.
