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
import os.path
import re
import hashlib


def convert_line(line):
    """
    Converts a single line of Markdown to HTML.

    Args:
        line (str): The Markdown line to convert.

    Returns:
        str: The converted HTML line.
    """
    # Bold syntax markdown to html
    line = line.replace('**', '<b>', 1)
    line = line.replace('**', '</b>', 1)
    line = line.replace('__', '<em>', 1)
    line = line.replace('__', '</em>', 1)

    # Md5
    md5 = re.findall(r'\[\[.+?\]\]', line)
    md5_inside = re.findall(r'\[\[(.+?)\]\]', line)
    if md5:
        line = line.replace(md5[0], hashlib.md5(
            md5_inside[0].encode()).hexdigest())

    # Removing the letter C
    remove_letter_c = re.findall(r'\(\(.+?\)\)', line)
    remove_c_more = re.findall(r'\(\((.+?)\)\)', line)
    if remove_letter_c:
        remove_c_more = ''.join(
            c for c in remove_c_more[0] if c not in 'Cc')
        line = line.replace(remove_letter_c[0], remove_c_more)

    return line


def process_line(line, html, unordered_start, ordered_start, paragraph):
    """
    Processes a single line of Markdown and writes the corresponding HTML.

    Args:
        line (str): The Markdown line to process.
        html (file): The HTML file to write to.
        unordered_start (bool): Indicates if an unordered list is open.
        ordered_start (bool): Indicates if an ordered list is currently open.
        paragraph (bool): Indicates if a paragraph is currently open.

    Returns:
        tuple: Updated values of unordered_start, ordered_start, and paragraph.
    """
    length = len(line)
    headings = line.lstrip('#')
    heading_num = length - len(headings)
    unordered = line.lstrip('-')
    unordered_num = length - len(unordered)
    ordered = line.lstrip('*')
    ordered_num = length - len(ordered)

    # Headings and Lists
    if 1 <= heading_num <= 6:
        line = '<h{}>'.format(
            heading_num) + headings.strip() + '</h{}>\n'.format(
            heading_num)

    if unordered_num:
        if not unordered_start:
            html.write('<ul>\n')
            unordered_start = True
        line = '<li>' + unordered.strip() + '</li>\n'
    if unordered_start and not unordered_num:
        html.write('</ul>\n')
        unordered_start = False

    if ordered_num:
        if not ordered_start:
            html.write('<ol>\n')
            ordered_start = True
        line = '<li>' + ordered.strip() + '</li>\n'
    if ordered_start and not ordered_num:
        html.write('</ol>\n')
        ordered_start = False

    if not (heading_num or unordered_start or ordered_start):
        if not paragraph and length > 1:
            html.write('<p>\n')
            paragraph = True
        elif length > 1:
            html.write('<br/>\n')
        elif paragraph:
            html.write('</p>\n')
            paragraph = False

    if length > 1:
        html.write(line)

    return unordered_start, ordered_start, paragraph


def process_markdown(input_file, output_file):
    """
    Converts a Markdown file to HTML.

    Args:
        input_file (str): The name of the Markdown file to convert.
        output_file (str): The name of the HTML file to create.

    Returns:
        None
    """
    # Check that the Markdown file exists and is a file
    if not os.path.isfile(input_file):
        print('Missing {}'.format(input_file), file=sys.stderr)
        exit(1)

    # Read the Markdown file
    with open(input_file) as read:
        with open(output_file, 'w') as html:
            unordered_start, ordered_start, paragraph = False, False, False
            # Process each line
            for line in read:
                line = convert_line(line)
                unordered_start, ordered_start, paragraph = process_line(
                    line, html, unordered_start, ordered_start, paragraph)

            if unordered_start:
                html.write('</ul>\n')
            if ordered_start:
                html.write('</ol>\n')
            if paragraph:
                html.write('</p>\n')


if __name__ == '__main__':
    # Check the number of arguments
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)

    process_markdown(sys.argv[1], sys.argv[2])
    
    # Exit with a successful status code
    exit(0)
