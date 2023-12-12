#!/usr/bin/python3
"""
markdown2html.py

A script that converts Markdown to HTML.

Usage:
    ./markdown2html.py README.md README.html

Arguments:
    input_file (str): The name of the Markdown file to convert.
        Default is "README.md".
    output_file (str): The name of the HTML file to create.
        Default is "README.html".
"""

import sys
import os
import re
import hashlib


def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to HTML and writes the output to a file.

    Args:
        input_file (str): The name of the Markdown file to convert.
        output_file (str): The name of the HTML file to create.

    Raises:
        SystemExit: If the number of arguments is less than 2 or
        if the Markdown file is missing.

    Returns:
        None
    """
    # Check the number of arguments
    if len(sys.argv) < 2:
        print(
            "Usage: ./markdown2html.py README.md README.html",
            file=sys.stderr)
        sys.exit(1)

    # Set default input and output files if not provided
    input_file = sys.argv[1] if len(sys.argv) >= 2 else "README.md"
    output_file = sys.argv[2] if len(sys.argv) >= 3 else "README.html"

    # Check that the Markdown file exists and is a file
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file
    with open(input_file, encoding="utf-8") as f:
        markdown_content = f.read()

    # Convert Markdown to HTML
    html_content = markdown_to_html(markdown_content)

    # Write the HTML output to a file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

def markdown_to_html(markdown_content):
    """
    Convert Markdown to HTML using regular expressions.

    Args:
        markdown_content (str): The content of the Markdown file.

    Returns:
        str: The HTML content.
    """
    # Regular expression for headings (up to level 6)
    heading_pattern = re.compile(r"^(#{1,6}) (.*)$", re.MULTILINE)
    # Regular expression for unordered lists
    ul_pattern = re.compile(r'^\s*-\s+([^\n]*(?:\n\s*-\s+[^\n]*)*)', re.MULTILINE)
    # Regular expression for ordered lists
    ol_pattern = re.compile(r'^\s*\*\s+([^\n]*(?:\n\s*\*\s+[^\n]*)*)', re.MULTILINE)
    # Regular expression for bold text
    bold_pattern = re.compile(r'\*\*(.+?)\*\*')
    # Regular expression for emphasized text
    emphasis_pattern = re.compile(r'__(.+?)__')
    # Regular expression for MD5 conversion
    md5_pattern = re.compile(r'\[\[(.+?)\]\]')
    # Regular expression for removing characters
    remove_chars_pattern = re.compile(r'\(\((.+?)\)\)', re.MULTILINE)
    # Regular expression for paragraph text
    # md_pattern = re.compile(r'^(.+?)$', re.MULTILINE)

    # Replace Markdown elements with corresponding HTML
    html_content = re.sub(heading_pattern, convert_heading, markdown_content)
    html_content = re.sub(ul_pattern, convert_ul, html_content)
    html_content = re.sub(ol_pattern, convert_ol, html_content)
    #html_content = re.sub(md_pattern, convert_md, html_content)
    html_content = re.sub(bold_pattern, r'<b>\1</b>', html_content)
    html_content = re.sub(emphasis_pattern, r'<em>\1</em>', html_content)

    # Process MD5 conversion
    matches = re.findall(md5_pattern, html_content)
    for match in matches:
        hashed = hashlib.md5(match.encode()).hexdigest()
        html_content = html_content.replace(f'[[{match}]]', hashed)

    # Remove characters as specified
    html_content = re.sub(remove_chars_pattern, convert_remove_chars, html_content)

    return html_content

def convert_heading(match):
    """
    Converts heading matches to HTML tags.

    Args:
        match (re.Match): The regular expression match object.

    Returns:
        str: The HTML heading tag.
    """
    heading_level = len(match.group(1))
    heading_text = match.group(2)
    heading_tag = f"<h{heading_level}>{heading_text}</h{heading_level}>"
    return heading_tag


def convert_ul(match):
    """
    Converts unordered list matches to HTML tags.

    Args:
        match (re.Match): The regular expression match object.

    Returns:
        str: The HTML unordered list tag.
    """
    items = match.group(1).split('\n')
    list_items = "\n".join(
        f"<li>{item.strip('-').strip()}</li>" for item in items if item.strip())
    ul_tag = f"<ul>\n{list_items}\n</ul>"
    return ul_tag


def convert_ol(match):
    """
    Converts ordered list matches to HTML tags.

    Args:
        match (re.Match): The regular expression match object.

    Returns:
        str: The HTML ordered list tag.
    """
    items = match.group(1).split('\n')
    list_items = "\n".join(
        f"<li>{item.strip('*').strip()}</li>" for item in items if item.strip())
    ol_tag = f"<ol>\n{list_items}\n</ol>"
    return ol_tag


def convert_md(match):
    """
    Converts paragraph text matches to HTML tags.

    Args:
        match (re.Match): The regular expression match object.

    Returns:
        str: The HTML paragraph tag.
    """
    #lines = 
    # text = 
    # return f""


def convert_remove_chars(match):
    """
    Remove characters (in this case, the letter 'c') from the content.

    Args:
        match (re.Match): The regular expression match object.

    Returns:
        str: The content with specified characters removed.
    """
    return match.group(1).replace('c', '').replace('C', '')


# Only execute if the script is run directly, not when imported
if __name__ == "__main__":
    # Get the input and output file names from the command-line arguments
    input_file = sys.argv[1] if len(sys.argv) >= 2 else "README.md"
    output_file = sys.argv[2] if len(sys.argv) >= 3 else "README.html"

    # Convert the Markdown file to HTML and write the output to a file
    convert_markdown_to_html(input_file, output_file)

    # Exit with a successful status code
    sys.exit(0)
