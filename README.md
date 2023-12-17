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
- [Tasks](#tasks)
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

## Tasks

### 0. Start a script

Write a script `markdown2html.py` that takes two string arguments:

- First argument: Name of the Markdown file
- Second argument: Output file name

**Requirements:**

- If the number of arguments is less than 2, print in STDERR: "Usage: ./markdown2html.py README.md README.html" and exit 1.
- If the Markdown file doesn’t exist, print in STDERR: "Missing <filename>" and exit 1.
- Otherwise, print nothing and exit 0.

**Example:**

```bash
$ ./markdown2html.py
Usage: ./markdown2html.py README.md README.html
$ ./markdown2html.py README.md README.html
Missing README.md
$ echo "Test" > README.md
$ ./markdown2html.py README.md README.html
```

**Repo:**

- [GitHub Repository: alx-frontend-for-fun](https://github.com/Dr-dyrane/alx-frontend-for-fun)
- **File:** [markdown2html.py](https://github.com/Dr-dyrane/alx-frontend-for-fun/markdown2html.py)

### 1. Headings

Improve `markdown2html.py` by parsing Headings Markdown syntax for generating HTML.

**Syntax:**

```markdown
# Heading level 1
## Heading level 2
### Heading level 3
#### Heading level 4
##### Heading level 5
###### Heading level 6
```

**Example:**

```bash
$ cat README.md
# My title
## My title2
# My title3
#### My title4
### My title5

$ ./markdown2html.py README.md README.html
$ cat README.html
<h1>My title</h1>
<h2>My title2</h2>
<h1>My title3</h1>
<h4>My title4</h4>
<h3>My title5</h3>
```

**Repo:**

- [GitHub Repository: alx-frontend-for-fun](https://github.com/Dr-dyrane/alx-frontend-for-fun)
- **File:** [markdown2html.py](https://github.com/Dr-dyrane/alx-frontend-for-fun/markdown2html.py)

### 2. Unordered Listing

Improve `markdown2html.py` by parsing Unordered Listing syntax for generating HTML.

**Syntax:**

```markdown
- Hello
- Bye
```

**Example:**

```bash
$ cat README.md
# My title
- Hello
- Bye

$ ./markdown2html.py README.md README.html
$ cat README.html
<h1>My title</h1>
<ul>
    <li>Hello</li>
    <li>Bye</li>
</ul>
```

**Repo:**

- [GitHub Repository: alx-frontend-for-fun](https://github.com/Dr-dyrane/alx-frontend-for-fun)
- **File:** [markdown2html.py](https://github.com/Dr-dyrane/alx-frontend-for-fun/markdown2html.py)

### 3. Ordered Listing

Improve `markdown2html.py` by parsing Ordered Listing syntax for generating HTML.

**Syntax:**

```markdown
* Hello
* Bye
```

**Example:**

```bash
$ cat README.md
# My title
* Hello
* Bye

$ ./markdown2html.py README.md README.html
$ cat README.html
<h1>My title</h1>
<ol>
    <li>Hello</li>
    <li>Bye</li>
</ol>
```

**Repo:**

- [GitHub Repository: alx-frontend-for-fun](https://github.com/Dr-dyrane/alx-frontend-for-fun)
- **File:** [markdown2html.py](https://github.com/Dr-dyrane/alx-frontend-for-fun/markdown2html.py)

### 4. Simple Text

Improve `markdown2html.py` by parsing paragraph syntax for generating HTML.

**Syntax:**

```markdown
Hello

I'm a text
with 2 lines
```

**Example:**

```bash
$ cat README.md
# My title
- Hello
- Bye

Hello

I'm a text
with 2 lines

$ ./markdown2html.py README.md README.html
$ cat README.html
<h1>My title</h1>
<ul>
    <li>Hello</li>
    <li>Bye</li>
</ul>
<p>
    Hello
</p>
<p>
    I'm a text
    <br />
    with 2 lines
</p>
```

**Repo:**

- [GitHub Repository: alx-frontend-for-fun](https://github.com/Dr-dyrane/alx-frontend-for-fun)
- **File:** [markdown2html.py](https://github.com/Dr-dyrane/alx-frontend-for-fun/markdown2html.py)

Certainly! Let's update the task descriptions for Task 5 with a similar table format for better clarity:

### 5. Bold and Emphasis Text

Improve `markdown2html.py` by parsing bold syntax for generating HTML.

**Syntax:**

```markdown
**Hello**
__Hello__
```

**HTML Generation:**

Markdown | HTML Generated
---------|----------------
`**Hello**` | `<b>Hello</b>`
`__Hello__` | `<em>Hello</em>`

**Example:**

```bash
$ cat README.md
# My title
- He**l**lo
- Bye

Hello

I'm **a** text
with __2 lines__

**Or in bold**

$ ./markdown2html.py README.md README.html
$ cat README.html
<h1>My title</h1>
<ul>
    <li>He<b>l</b>lo</li>
    <li>Bye</li>
</ul>
<p>
    Hello
</p>
<p>
    I'm <b>a</b> text
    <br/>
    with <em>2 lines</em>
</p>
<p>
    <b>Or in bold</b>
</p>
```

**Repo:**

- [GitHub Repository: alx-frontend-for-fun](https://github.com/Dr-dyrane/alx-frontend-for-fun)
- **File:** [markdown2html.py](https://github.com/Dr-dyrane/alx-frontend-for-fun/markdown2html.py)

### 6. ... but why??

Improve `markdown2html.py` by parsing specific syntax for generating HTML.

**Syntax:**

```markdown
[[Hello]]
((Hello Chicago))
```

**HTML Generation and Description:**

Markdown | HTML Generated | Description
---------|----------------|-------------
`[[Hello]]` | `8b1a9953c4611296a827abf8c47804d7` | Convert in MD5 (lowercase) the content
`((Hello Chicago))` | `Hello hiago` | Remove all `c` (case-insensitive) from the content

**Example:**

```bash
$ cat README.md
# My title
- He**l**lo
- Bye

Hello

I'm **a** text
with __2 lines__

((I will live in Caracas))

But it's [[private]]

So cool!

$ ./markdown2html.py README.md README.html
$ cat README.html
<h1>My title</h1>
<ul>
    <li>He<b>l</b>lo</li>
    <li>Bye</li>
</ul>
<p>
    Hello
</p>
<p>
    I'm <b>a</b> text
    <br/>
    with <em>2 lines</em>
</p>
<p>
    I will live in araas
</p>
<p>
    But it's 2c17c6393771ee3048ae34d6b380c5ec
</p>
<p>
    So cool!
</p>
```
**Repo:**

- [GitHub Repository: alx-frontend-for-fun](https://github.com/Dr-dyrane/alx-frontend-for-fun)
- **File:** [markdown2html.py](https://github.com/Dr-dyrane/alx-frontend-for-fun/markdown2html.py)

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

### Copyright

Copyright © 2023 ALX, All rights reserved.
