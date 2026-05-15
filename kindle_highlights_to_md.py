#!/usr/bin/env python3

import re
import argparse
from pathlib import Path
from typing import List, Dict, Optional


def parse_clippings(file_path: str) -> Dict[str, List[Dict]]:
    """Parse Kindle's My Clippings.txt into a structured dictionary."""
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        content = file.read()
    
    # Split into entries
    entries = re.split(r'==========\n', content)
    books = {}
    
    for entry in entries:
        if not entry.strip():
            continue
        
        # Extract book title, metadata, and content
        lines = entry.strip().split('\n')
        if len(lines) < 3:
            continue
        
        title = lines[0].strip()
        metadata = lines[1].strip()
        content = '\n'.join(lines[2:]).strip()
        
        # Parse metadata (e.g., "- Your Highlight on Location 123-124 | Added on Monday, June 1, 2020")
        metadata_parts = re.match(
            r'- Your (Highlight|Note) on (.*?) \| Added on (.*)',
            metadata
        )
        if not metadata_parts:
            continue
        
        highlight_type = metadata_parts.group(1)
        location = metadata_parts.group(2)
        date = metadata_parts.group(3)
        
        # Add to book dictionary
        if title not in books:
            books[title] = []
        books[title].append({
            'type': highlight_type.lower(),
            'content': content,
            'location': location,
            'date': date
        })
    
    return books


def generate_markdown(books: Dict[str, List[Dict]], output_dir: str) -> None:
    """Generate Markdown files for each book."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    for title, highlights in books.items():
        # Sanitize title for filename
        safe_title = re.sub(r'[^a-zA-Z0-9]', '_', title)
        md_file = output_path / f"{safe_title}.md"
        
        with open(md_file, 'w', encoding='utf-8') as file:
            file.write(f"# {title}\n\n")
            
            for highlight in highlights:
                file.write(f"## {highlight['type'].capitalize()}\n")
                file.write(f"**Location**: {highlight['location']} | **Date**: {highlight['date']}\n\n")
                file.write(f"{highlight['content']}\n\n")
                file.write("---\n\n")


def main():
    parser = argparse.ArgumentParser(description='Convert Kindle highlights to Markdown.')
    parser.add_argument('--input', type=str, required=True, help='Path to My Clippings.txt')
    parser.add_argument('--output', type=str, required=True, help='Output directory for Markdown files')
    args = parser.parse_args()
    
    books = parse_clippings(args.input)
    generate_markdown(books, args.output)
    print(f"Generated Markdown files in {args.output}")


if __name__ == '__main__':
    main()