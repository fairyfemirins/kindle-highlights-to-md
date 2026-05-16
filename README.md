# Kindle Highlights to Markdown CLI

Convert Kindle's `My Clippings.txt` into Markdown files for Obsidian, Logseq, or any note-taking app.

## Features
- Parse `My Clippings.txt` (Kindle's default export format).
- Extract highlights, notes, and book metadata (Page, Location, Date).
- Output to Markdown (compatible with Obsidian, Logseq).
- Support for **Kobo** and **Apple Books** (future extensibility).

## Installation
```bash
pip install --user .
```

## Usage
```bash
kindle2md "My Clippings.txt" ./output
```

## Example Output
```markdown
# The Pragmatic Programmer (Andrew Hunt)

> Debugging is twice as hard as writing the code in the first place.

**Page 42** | **Location 642-643** | **Saturday, May 16, 2026 05:45:00 AM**
---

> Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.

**Page 43** | **Location 650-651** | **Saturday, May 16, 2026 05:46:00 AM**
---
```

## License
MIT License. See [LICENSE](LICENSE).