#!/usr/bin/python3
"""
A script that converts Markdown to HTML.
"""

import sys
import os
import re


def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to HTML and writes the output to a file.
    """
    # Check that the Markdown file exists and is a file
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file
    with open(input_file, encoding="utf-8") as f:
        markdown_content = f.read()

    # Convert Markdown to HTML using regular expressions
    html_content = markdown_to_html(markdown_content)

    # Write the HTML output to a file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)


def markdown_to_html(markdown_content):
    """
    Convert Markdown to HTML using regular expressions
    """
    # Regular expression for headings (up to level 6)
    heading_pattern = re.compile(r'^(#+) (.*)$', re.MULTILINE)
    # Regular expression for unordered lists
    ul_pattern = re.compile(r'^\s*-\s+(.+)$', re.MULTILINE)
    # Regular expression for ordered lists
    ol_pattern = re.compile(r'^\s*\*\s+(.+)$', re.MULTILINE)
    # Regular expression for bold text
    bold_pattern = re.compile(r'\*\*(.+?)\*\*')

    # Replace Markdown elements with corresponding HTML
    html_content = re.sub(heading_pattern, r'<h\1>\2</h\1>', markdown_content)
    html_content = re.sub(
        ul_pattern, r'<ul>\n<li>\1</li>\n</ul>', html_content)
    html_content = re.sub(
        ol_pattern, r'<ol>\n<li>\1</li>\n</ol>', html_content)
    html_content = re.sub(bold_pattern, r'<b>\1</b>', html_content)

    return html_content


if __name__ == "__main__":
    # Check that the correct number of arguments were provided
    if len(sys.argv) != 3:
        print(
            "Usage: ./markdown2html.py <input_file> <output_file>",
            file=sys.stderr
        )
        sys.exit(1)

    # Get the input and output file names from the command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert the Markdown file to HTML and write the output to a file
    convert_markdown_to_html(input_file, output_file)

    # Exit with a successful status code
    sys.exit(0)
