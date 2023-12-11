# Markdown to HTML Converter

## Project Overview

This project aims to create a Markdown to HTML converter, allowing users to convert Markdown files to HTML format. The converter supports various Markdown syntax elements, including headings, lists, paragraphs, and text formatting.

## Author

- **Author:** Alexander Udeogaranya
- **Email:** Ogranya.alex@gmail.com
- **GitHub Username:** [Dr-dyrane](https://github.com/Dr-dyrane)

## Table of Contents

- [Project Overview](#project-overview)
- [Author](#author)
- [Table of Contents](#table-of-contents)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Usage](#usage)
  - [Script Execution](#script-execution)
  - [Markdown Syntax Supported](#markdown-syntax-supported)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project has the following structure:

- `markdown2html.py`: The main script for converting Markdown to HTML.
- `README.md`: Project documentation in Markdown format.

## Requirements

- Ubuntu 18.04 LTS
- Python 3.7 or higher
- PEP 8 style (version 1.7.x)
- Executable files
- Documented code
- ...

## Usage

### Script Execution

To convert a Markdown file to HTML, run the following command:

```bash
./markdown2html.py input_file.md output_file.html
```

### Markdown Syntax Supported

The converter supports the following Markdown syntax:

- Headings (`#`, `##`, ..., `######`)
- Unordered Lists (`-`)
- Ordered Lists (`*`)
- Paragraphs
- Bold Text (`**text**`)
- Emphasis Text (`__text__`)
- Custom Syntax (e.g., `[[text]]`, `((text))`)

## Examples

### Example 1

```bash
./markdown2html.py sample.md output.html
```

This command converts the contents of `sample.md` to HTML and saves the result in `output.html`.

### Example 2

```bash
./markdown2html.py README.md result.html
```

Converts the project's README file to HTML, saving the result in `result.html`.

## Contributing

If you would like to contribute to the project, please follow the guidelines outlined in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
