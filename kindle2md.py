#!/usr/bin/env python3
import re
import argparse
from pathlib import Path
from typing import List, Dict

def parse_clippings(file_path: str) -> Dict[str, List[Dict]]:
    """Parse Kindle's 'My Clippings.txt' into structured data."""
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    # Split entries by separator
    entries = re.split(r'==========\n', content)
    books = {}

    for entry in entries:
        if not entry.strip():
            continue
        lines = entry.strip().split('\n')
        if len(lines) < 3:
            continue

        # Extract book title, metadata, and highlight
        book_title = lines[0].strip()
        metadata = lines[1].strip()
        highlight = '\n'.join(lines[3:]).strip()

        # Parse metadata (e.g., "- Your Highlight on Page 42 | Location 642-643 | Added on Saturday, May 16, 2026 05:45:00 AM")
        meta_parts = re.split(r' \| ', metadata)
        page = location = date = None
        for part in meta_parts:
            if 'Page' in part:
                page = part.split('Page ')[1].split(' ')[0]
            elif 'Location' in part:
                location = part.split('Location ')[1].split(' ')[0]
            elif 'Added on' in part:
                date = ' '.join(part.split(' ')[2:])

        if book_title not in books:
            books[book_title] = []
        books[book_title].append({
            'highlight': highlight,
            'page': page,
            'location': location,
            'date': date
        })

    return books

def export_to_markdown(books: Dict[str, List[Dict]], output_dir: str) -> None:
    """Export parsed highlights to Markdown files."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for book_title, highlights in books.items():
        # Sanitize filename
        safe_title = re.sub(r'[\\/*?:"<>|]', '', book_title)
        md_file = output_path / f"{safe_title}.md"

        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(f"# {book_title}\n\n")
            for highlight in highlights:
                f.write(f"> {highlight['highlight']}\n\n")
                if highlight['page']:
                    f.write(f"**Page {highlight['page']}** | ")
                if highlight['location']:
                    f.write(f"**Location {highlight['location']}** | ")
                if highlight['date']:
                    f.write(f"**{highlight['date']}**\n\n")
                else:
                    f.write("\n")
                f.write("---\n\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Kindle highlights to Markdown.')
    parser.add_argument('input', help='Path to My Clippings.txt')
    parser.add_argument('output', help='Output directory for Markdown files')
    args = parser.parse_args()

    books = parse_clippings(args.input)
    export_to_markdown(books, args.output)
    print(f"Exported {len(books)} books to {args.output}")