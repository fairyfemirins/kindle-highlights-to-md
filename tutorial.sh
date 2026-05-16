#!/bin/bash
# Reproducible Tutorial: Kindle Highlights to Markdown

# 1. Clone the repo
mkdir -p ~/kindle-highlights && cd ~/kindle-highlights
git clone https://github.com/femirins/kindle-highlights-to-md.git
cd kindle-highlights-to-md

# 2. Prepare your Kindle clippings
# Copy "My Clippings.txt" from your Kindle to this directory:
# cp /path/to/Kindle/documents/My\ Clippings.txt ./

# 3. Run the tool
python3 kindle_highlights.py --input "My Clippings.txt" --output "highlights.md"

# 4. View the output
cat highlights.md