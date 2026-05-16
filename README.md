# Kindle Highlights to Markdown CLI

![License](https://img.shields.io/badge/license-MIT-blue.svg)

A CLI tool to convert Kindle's `My Clippings.txt` into structured Markdown for note-taking apps (Obsidian, Notion, Logseq).

## Features
- ✅ Parse `My Clippings.txt` into structured Markdown.
- ✅ Group highlights by book.
- ✅ Preserve metadata (page numbers, timestamps).
- ✅ Export to Obsidian, Notion, or plain Markdown.

## Installation
```bash
pip install kindle-highlights-to-md
```

## Usage
```bash
python3 kindle_highlights.py --input "My Clippings.txt" --output "highlights.md"
```

## Example Output
```markdown
# Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones

- You do not rise to the level of your goals. You fall to the level of your systems.
  *- Your Highlight on page 15 | Location 224-225 | Added on Saturday, May 16, 2026 01:25:12 AM*

---
```

## Roadmap
- [ ] Support for Kobo/other e-readers.
- [ ] Tagging system for highlights.
- [ ] Direct Obsidian/Notion integration.

## License
MIT