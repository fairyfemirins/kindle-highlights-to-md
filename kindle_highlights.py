#!/usr/bin/env python3
"""
Kindle Highlights to Markdown CLI

Parses Kindle's 'My Clippings.txt' and exports highlights to structured Markdown.
Usage:
  python3 kindle_highlights.py --input "My Clippings.txt" --output "highlights.md"
"""

import re
import argparse
from pathlib import Path
from typing import List, Dict


def parse_clippings(file_path: str) -> Dict[str, List[Dict]]:
    """Parse Kindle's 'My Clippings.txt' into a structured dict with metadata."""
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    # Split entries by "==========" delimiter
    entries = re.split(r'\r?\n==========\r?\n', content)
    
    # Remove test file header if present
    if "Sample My Clippings.txt for testing" in entries[0]:
        entries = entries[1:]
    
    books = {}
    for entry in entries:
        if not entry.strip():
            continue
        
        # Extract book title, highlight, and metadata
        lines = entry.strip().split('\n')
        if len(lines) < 3:
            continue
            
        book_title = lines[0].strip().split('(')[0].strip()  # Remove author/parentheses
        metadata = lines[1].strip()  # e.g., "- Your Highlight on page 42 | Location 632-633 | Added on Saturday, May 16, 2026 01:20:41 AM"
        highlight = '\n'.join(lines[3:]).strip().split('==========')[0].strip()  # Remove trailing delimiter
        
        if book_title not in books:
            books[book_title] = []
        books[book_title].append({
            "highlight": highlight,
            "metadata": metadata
        })
    
    return books


def export_to_markdown(books: Dict[str, List[Dict]], output_path: str) -> None:
    """Export parsed highlights to Markdown with metadata."""
    with open(output_path, 'w', encoding='utf-8') as f:
        for book_title, highlights in books.items():
            f.write(f"# {book_title}\n\n")
            for item in highlights:
                f.write(f"- {item['highlight']}\n  *{item['metadata']}*\n\n")
            f.write("---\n\n")


def main():
    parser = argparse.ArgumentParser(description='Convert Kindle highlights to Markdown.')
    parser.add_argument('--input', type=str, required=True, help='Path to My Clippings.txt')
    parser.add_argument('--output', type=str, required=True, help='Output Markdown file')
    args = parser.parse_args()
    
    books = parse_clippings(args.input)
    export_to_markdown(books, args.output)
    print(f"✅ Exported {len(books)} books to {args.output}")


if __name__ == '__main__':
    main()