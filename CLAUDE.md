# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal documentation website built with MkDocs and hosted on GitHub Pages at tongsun99.github.io.

## Common Commands

### Development
```bash
mkdocs serve    # Start live-reloading dev server at http://127.0.0.1:8000
mkdocs build    # Build static site to site/ directory
```

### Building for Production
```bash
mkdocs build    # Generate production-ready static files in site/
```

### Deployment
The `site/` directory contains the built static files. For GitHub Pages deployment:
- The built site should be pushed to the repository
- GitHub Pages will serve from the root or the `/docs` folder depending on repository settings
- Alternatively, use `mkdocs gh-deploy` to automatically build and push to gh-pages branch

## Repository Structure

```
mkdocs.yml      # MkDocs configuration
docs/           # Source markdown files
  index.md      # Homepage
site/           # Built output (generated, typically gitignored)
```

## Architecture

This is a static site generator with a straightforward flow:
1. Markdown files in `docs/` are the content source
2. `mkdocs.yml` configures site metadata, theme, and navigation
3. Running `mkdocs build` generates static HTML/CSS/JS in `site/`
4. The `site/` directory is deployed to GitHub Pages

## Configuration

All site configuration is in `mkdocs.yml`:
- `site_name`: The site title
- Additional settings for theme, navigation, plugins, etc. can be added as needed

Refer to [MkDocs documentation](https://www.mkdocs.org) for available configuration options.
