import unittest
import tempfile
import shutil
from pathlib import Path
from kindle2md import parse_clippings, export_to_markdown

class TestKindle2MD(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.clippings_file = Path(self.test_dir) / "My Clippings.txt"
        self.clippings_file.write_text("""The Pragmatic Programmer (Andrew Hunt)
- Your Highlight on Page 42 | Location 642-643 | Added on Saturday, May 16, 2026 05:45:00 AM

Debugging is twice as hard as writing the code in the first place.
==========
The Pragmatic Programmer (Andrew Hunt)
- Your Highlight on Page 43 | Location 650-651 | Added on Saturday, May 16, 2026 05:46:00 AM

Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.
""")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_parse_clippings(self):
        books = parse_clippings(str(self.clippings_file))
        self.assertIn("The Pragmatic Programmer (Andrew Hunt)", books)
        self.assertEqual(len(books["The Pragmatic Programmer (Andrew Hunt)"]), 2)

    def test_export_to_markdown(self):
        books = parse_clippings(str(self.clippings_file))
        output_dir = Path(self.test_dir) / "output"
        export_to_markdown(books, str(output_dir))

        md_file = output_dir / "The Pragmatic Programmer (Andrew Hunt).md"
        self.assertTrue(md_file.exists())
        content = md_file.read_text()
        self.assertIn("Debugging is twice as hard", content)
        self.assertIn("Page 42", content)

if __name__ == '__main__':
    unittest.main()