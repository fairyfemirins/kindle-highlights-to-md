import pytest
from kindle_highlights_to_md import parse_clippings, generate_markdown
from pathlib import Path
import shutil


def test_parse_clippings():
    """Test parsing of My Clippings.txt."""
    test_file = "test_clippings.txt"
    with open(test_file, 'w', encoding='utf-8') as file:
        file.write("""Sample Book Title
- Your Highlight on Location 123-124 | Added on Monday, June 1, 2020
This is a highlight.\n
==========\nSample Book Title
- Your Note on Location 456 | Added on Tuesday, June 2, 2020
This is a note.\n
==========\n""")
    
    books = parse_clippings(test_file)
    assert 'Sample Book Title' in books
    assert len(books['Sample Book Title']) == 2
    assert books['Sample Book Title'][0]['type'] == 'highlight'
    assert books['Sample Book Title'][1]['type'] == 'note'
    
    # Cleanup
    Path(test_file).unlink()


def test_generate_markdown():
    """Test Markdown generation."""
    books = {
        'Sample Book Title': [
            {
                'type': 'highlight',
                'content': 'This is a highlight.',
                'location': '123-124',
                'date': 'Monday, June 1, 2020'
            }
        ]
    }
    output_dir = 'test_output'
    generate_markdown(books, output_dir)
    
    md_file = Path(output_dir) / 'Sample_Book_Title.md'
    assert md_file.exists()
    
    # Cleanup
    shutil.rmtree(output_dir)


if __name__ == '__main__':
    pytest.main()