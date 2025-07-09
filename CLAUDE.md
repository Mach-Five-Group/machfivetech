# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the Mach Five Tech Group website (www.MachFiveTech.com), a static site hosted on GitHub Pages. It's a marketing/corporate website showcasing software development services, technical leadership expertise, and knowledge base articles.

## Architecture & Structure

### Technology Stack
- **Pure HTML/CSS/JavaScript** - No build process or modern frameworks
- **Neodigm55 UI Framework** - External library loaded via CDN
- **SimplexNoise** - For animated canvas backgrounds
- **GitHub Pages** - Hosting platform (gh-pages branch)

### Directory Organization
- `/` - Root contains main pages (index.html, privacy-policy.html)
- `/services/` - Individual service offering pages (code/, culture/, delight/, etc.)
- `/knowledge-base/` - Technical articles and blog posts
- `/img/` - All image assets
- `/js/` - JavaScript files (shift.js for animations, util.js for utilities)
- `/design/` - Source design files (Affinity Designer/Photo)

### Key Files
- `shift.js` - Handles animated background effects using canvas and SimplexNoise
- `util.js` - Utility functions for the site
- `site.webmanifest` - PWA configuration
- `CNAME` - Points to www.MachFiveTech.com

## Development Guidelines

### Working with Pages
- Each major section is a separate HTML file
- Consistent header/navigation structure across pages
- CSS custom properties used for theming (--color-*, --transition-*, etc.)
- Material Symbols icons used throughout

### Adding New Content
- Service pages follow the pattern `/services/[service-name]/index.html`
- Knowledge base articles go in `/knowledge-base/`
- Images should be optimized and placed in `/img/`

### Deployment
- All changes are made directly to the gh-pages branch
- GitHub Pages automatically deploys changes
- No build or compilation step required

### Common Tasks
Since this is a static site with no build process:
- **Preview changes**: Open HTML files directly in browser or use a local server
- **Deploy**: Push changes to gh-pages branch
- **Add new page**: Create HTML file following existing page structure
- **Update navigation**: Modify nav elements across relevant pages

### Important Notes
- Neodigm55 framework provides UI components and animations
- Canvas animations in shift.js can impact performance
- Mobile responsiveness handled through viewport meta tags and CSS
- No JavaScript framework means manual DOM manipulation when needed