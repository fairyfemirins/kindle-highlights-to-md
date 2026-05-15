# Kindle Highlights to Markdown

**Convert Kindle highlights into structured Markdown files.**

## Overview
This CLI tool parses Kindle's `My Clippings.txt` file and generates a Markdown file for each book, preserving highlights, notes, and timestamps.

## Features
- Parse `My Clippings.txt` into book-specific Markdown files.
- Preserve highlights, notes, and timestamps.
- Support for nested notes and tags.
- Customizable output templates (future extension).

## Technical Architecture
1. **Parser**: Uses regex to split `My Clippings.txt` into entries and extract metadata (title, location, date).
2. **Generator**: Writes Markdown files with a structured format (book title, highlight type, location, date, content).
3. **CLI**: argparse for input/output arguments.

## Installation
```bash
pip install kindle-highlights-to-md
```

## Usage
```bash
kindle-highlights-to-md --input "My Clippings.txt" --output "output_directory"
```

## Example Output
```markdown
# Sample Book Title

## Highlight
**Location**: 123-124 | **Date**: Monday, June 1, 2020

This is a highlight.

---

## Note
**Location**: 456 | **Date**: Tuesday, June 2, 2020

This is a note.

---
```

## License
MIT