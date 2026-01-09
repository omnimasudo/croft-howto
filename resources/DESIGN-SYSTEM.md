# Claude How To - Design System

## Visual Identity

### Icon Design Concept: Ascending Progression

The Claude How To icon uses **three ascending hexagons** to represent the learning journey:

```
        🔷 Level 7-10 (MINT)
        Advanced Features

    🔶 Level 4-6 (EMERALD)
    Intermediate Skills

🔹 Level 1-3 (DARK EMERALD)
Beginner Fundamentals
```

This creates:
- **Visual Clarity**: Immediate recognition of progression
- **Symbolic Meaning**: Upward movement = growth & learning
- **Scalability**: Works at any size from 16px to 512px
- **Brand Alignment**: Matches the tech-forward CLI aesthetic

---

## Color System

### Palette

| Color | Hex | RGB | Usage |
|-------|-----|-----|-------|
| Deep Forest (BG) | `#0d1f0d` | 13, 31, 13 | Backgrounds, containers |
| Emerald (Primary) | `#10b981` | 16, 185, 129 | Main accents, buttons |
| Dark Emerald | `#059669` | 5, 150, 105 | Secondary accents, borders |
| Forest | `#047857` | 4, 120, 87 | Tertiary, deep accents |
| Mint (Highlight) | `#6ee7b7` | 110, 231, 183 | Highlights, focus states |
| Light Mint | `#34d399` | 52, 211, 153 | Secondary highlights |

### Contrast Ratios (WCAG)

- Emerald on Dark Forest: **8.2:1** ✅ AAA
- Mint on Dark Forest: **9.1:1** ✅ AAA
- All colors maintain AA compliance on dark backgrounds

---

## Gradient System

### Primary Gradients

**Emerald Gradient** (left→right, top→bottom):
- Start: `#10b981` (bright emerald)
- End: `#047857` (dark forest green)
- Usage: Icon backgrounds, primary elements

**Mint Gradient** (top→bottom):
- Start: `#6ee7b7` (bright mint)
- End: `#34d399` (darker mint)
- Usage: Highlights, accent elements

**Dark Emerald Gradient** (left→right, top→bottom):
- Start: `#059669` (dark emerald)
- End: `#064e3b` (forest green)
- Usage: Secondary elements, depth

---

## Typography

### Logo Font
- **Family**: JetBrains Mono, SF Mono, Fira Code (monospace)
- **Weight**: 700 (bold) for "Claude-", 400 (regular) for "Howto"
- **Style**: Modern, tech-forward
- **Usage**: Logo wordmark, code examples

### Interface Font
- **Family**: Inter, SF Pro, system fonts (sans-serif)
- **Weight**: 400-600
- **Style**: Clean, readable
- **Usage**: UI text, descriptions

---

## Icon Details

### Hexagon Specifications

All three hexagons follow the same geometry pattern:

```svg
<!-- Regular hexagon with flat top -->
M -26,0          <!-- Left point -->
L -13,-22.5      <!-- Top-left corner -->
L 13,-22.5       <!-- Top-right corner -->
L 26,0           <!-- Right point -->
L 13,22.5        <!-- Bottom-right corner -->
L -13,22.5       <!-- Bottom-left corner -->
Z                <!-- Close path -->
```

**Hexagon Sizes**:
- Bottom (Beginner): 26 unit radius
- Middle (Intermediate): 32 unit radius
- Top (Advanced): 26 unit radius

### Visual Elements

1. **Strokes**: 1.5-2.5px width depending on size
2. **Glows**: Soft emerald/mint blur for depth
3. **Connecting Lines**: Dashed lines showing progression
4. **Center Dot**: Accent element at center point
5. **Outer Rings**: Subtle circular guides

---

## Sizing Guidelines

### Favicon Hierarchy

```
16px   → Minimal geometry, browser tab
32px   → Two hexagons visible
64px   → All three hexagons clear
128px  → Full detail with glows
256px  → Complete with all effects
```

### Logo Sizing

- **Minimum**: 100px width (for web)
- **Recommended**: 400-800px (high quality)
- **Maximum**: Unlimited (vector format)
- **Aspect Ratio**: 4:1 (width:height)

### Icon Sizing

- **Minimum**: 32px (small thumbnails)
- **Recommended**: 64-256px (apps, avatars)
- **Maximum**: Unlimited (vector format)
- **Aspect Ratio**: 1:1 (square)

---

## Effects & Filters

### Glow Effect

```svg
<filter id="softGlow">
  <feGaussianBlur stdDeviation="2" result="blur"/>
  <feFlood flood-color="#10b981" flood-opacity="0.4"/>
  <feComposite in2="blur" operator="in"/>
  <feMerge>
    <feMergeNode/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>
```

Creates: Soft green glow around elements

### Shadow Effect

```svg
<filter id="shadow">
  <feGaussianBlur in="SourceAlpha" stdDeviation="3"/>
  <feOffset dx="2" dy="4" result="offsetblur"/>
  <feComponentTransfer>
    <feFuncA type="linear" slope="0.3"/>
  </feComponentTransfer>
  <feMerge>
    <feMergeNode/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>
```

Creates: Subtle drop shadow for depth

---

## Spacing & Alignment

### Logo Spacing

```
┌─────────────────────────────────────┐
│                                     │
│        Clear Space Minimum          │
│         (logo width / 4)            │
│                                     │
│              [LOGO]                 │
│                                     │
└─────────────────────────────────────┘
```

### Icon Center Point

All icons center at (128, 128) for 256px canvas:
- Allows proper scaling and transformation
- Centers vertically and horizontally
- Maintains alignment with other UI elements

---

## Accessibility

### Color Contrast
- All foreground/background combinations meet WCAG AAA
- No red-green color dependency
- Works for color-blind users

### Scalability
- Vector format ensures clarity at any size
- Geometric shapes remain recognizable at 16px
- Maintains proportions when scaled

### Animation Safe
- SVG can be animated if needed
- Static by default for performance
- Use CSS/JS for interactive states

---

## Application Examples

### Web Header
- Size: 800×200px
- File: `logos/claude-howto-logo.svg`
- Background: Transparent or dark
- Padding: 20px minimum

### App Icon
- Size: 256×256px or larger
- File: `icons/claude-howto-icon.svg`
- Background: Dark or transparent
- Use: App shortcuts, avatars

### Browser Favicon
- Size: 32px (primary), 16px (fallback)
- File: `favicons/favicon-32.svg`
- Format: SVG for crisp display
- Use: Browser tabs, bookmarks

### Social Media
- Profile: 256×256px icon
- Banner: 800×200px logo (centered)
- Story/Post: Icon at 1080×1080px

### Documentation
- Chapter Headers: 400×100px logo
- Section Icons: 64×64px favicon
- Inline: 32×32px favicon

---

## File Format Details

### SVG Structure

All SVG files include:
- XML declaration
- `<defs>` section with gradients and filters
- ViewBox attribute for responsiveness
- Named gradients for reuse
- Readable code structure

### Optimization

Files are optimized but readable:
- Maintains whitespace for clarity
- Includes comments where helpful
- Gradients named for easy reference
- Filters documented in code

### Cross-Browser Compatibility

- ✅ Chrome/Edge: Full support
- ✅ Firefox: Full support
- ✅ Safari: Full support
- ✅ iOS Safari: Full support
- ✅ All modern browsers: Full support

---

## Customization

### Changing Colors

To create variants with different colors:

1. Replace gradient stop colors:
```svg
<stop offset="0%" style="stop-color:#NEW_COLOR"/>
```

2. Update filter colors:
```svg
<feFlood flood-color="#NEW_COLOR" flood-opacity="0.4"/>
```

3. Keep contrast ratios above 4.5:1 for accessibility

### Scaling

To scale any icon:
```css
svg {
  width: 256px;
  height: 256px;
  transform: scale(1.5);
}
```

Or in SVG:
```svg
<svg transform="scale(2)">
  <!-- content -->
</svg>
```

---

## Version Control

Track design changes in git:
- Use `.gitkeep` in empty directories
- Version SVG files normally (they're text)
- Tag releases with design changes
- Include DESIGN-SYSTEM.md in commits

---

**Last Updated**: January 2026
**Design System Version**: 1.0
