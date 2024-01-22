# Sass & Scss Short Specialization Project

## Overview

This project is part of the Short Specialization on Sass & Scss, focusing on front-end development. The curriculum is designed by Guillaume, CTO at Holberton School, and carries a weight of 1 in the overall assessment. The project is scheduled to start on Jan 22, 2024, at 6:00 AM, and must be completed by Jan 29, 2024, at 6:00 AM. The checker will be released on Jan 24, 2024, at 12:00 AM, with an auto review launched at the deadline.

## Learning Objectives

Upon completion of this project, you are expected to be able to explain the following concepts without the help of Google:

- What Sass means
- How to write Sass & Scss files
- The difference between Sass and Scss
- Sass preprocessing
- Variable declaration
- Nested definitions
- Importing Sass files
- Using mixins
- Declaring extend/inheritance styles
- Manipulating operators

In this Sass & Scss Short Specialization Project, you will gain a deep understanding of various concepts related to Sass and Scss, essential for effective front-end development. Let's delve into each learning objective with detailed explanations, pictorial examples, and code snippets.

## 1. What Sass means

**Explanation:**
Sass stands for "Syntactically Awesome Stylesheets." It is a preprocessor scripting language that is interpreted or compiled into Cascading Style Sheets (CSS). SassScript is the scripting language itself.

![Sass Logo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/5/9936ba361a3962278900.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240122%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240122T152302Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a7a1dd7d71b5bd3b96931a338a642fa8faaf9067810db76c909612239c895e05)

 Sass is a language that enhances the capabilities of CSS, providing features like variables, nesting, and more.

## 2. How to write Sass & Scss files

**Explanation:**
Sass files use the `.scss` extension, and they allow for a more concise and readable syntax compared to traditional CSS. The `.sass` extension is also available, using a different, indentation-based syntax.

**Code:**
```scss
/* Example SASS File */
body
  font-family: 'Arial', sans-serif
  color: #333
```

## 3. The difference between Sass and Scss

**Explanation:**
Sass has two syntax options: the original, whitespace-sensitive syntax (indicated by the `.sass` extension), and the newer SCSS syntax (`.scss`) that resembles traditional CSS with braces and semicolons.

**Pictorial Example:**
```scss
/* SCSS Syntax */
body {
  font-family: 'Arial', sans-serif;
  color: #333;
}
```

```sass
/* Sass Syntax */
body
  font-family: 'Arial', sans-serif
  color: #333
```

## 4. Sass preprocessing

**Explanation:**
Sass preprocessing involves translating Sass or Scss code into standard CSS before deploying it. This process allows developers to use advanced features not natively supported by CSS.

## 5. Variable declaration

**Explanation:**
Sass allows the use of variables to store reusable values. This promotes consistency and ease of maintenance by centralizing values that might be used across multiple styles.

**Code:**
```scss
/* Variable Declaration */
$primary-color: #3498db;

body {
  background-color: $primary-color;
}
```

## 6. Nested definitions

**Explanation:**
Sass provides nesting capabilities, allowing for a more structured and readable organization of styles, mirroring the HTML structure.

**Code:**
```scss
/* Nested Definitions */
nav {
  ul {
    margin: 0;
    padding: 0;
    list-style: none;

    li { display: inline-block; }

    a {
      text-decoration: none;
    }
  }
}
```

## 7. Importing Sass files

**Explanation:**
Sass allows the modularization of styles by importing one Sass file into another. This helps in maintaining a clean and organized codebase.

**Code:**
```scss
/* Importing Sass Files */
@import 'reset';
@import 'variables';

body {
  font-family: $base-font;
}
```

## 8. Using mixins

**Explanation:**
Mixins in Sass allow the reuse of blocks of styles. They are similar to functions in programming languages and promote code reusability.

**Code:**
```scss
/* Using Mixins */
@mixin border-radius($radius) {
  -webkit-border-radius: $radius;
  -moz-border-radius: $radius;
  border-radius: $radius;
}

.box {
  @include border-radius(10px);
}
```

## 9. Declaring extend/inheritance styles

**Explanation:**
Extend allows a selector to inherit styles from another selector. This promotes a cleaner and more maintainable style structure.

**Code:**
```scss
/* Declaring Extend/Inheritance Styles */
%message-shared {
  border: 1px solid #ccc;
  padding: 10px;
  color: #333;
}

.success {
  @extend %message-shared;
  border-color: green;
}

.error {
  @extend %message-shared;
  border-color: red;
}
```

## 10. Manipulating operators

**Explanation:**
Sass supports various mathematical operators, providing the ability to perform calculations within stylesheets.

**Code:**
```scss
/* Manipulating Operators */
$base-font-size: 16px;

body {
  font-size: $base-font-size * 1.5;
}
```

These learning objectives cover essential concepts in Sass and Scss. Understanding these principles will empower you to write more maintainable, modular, and efficient stylesheets for front-end development.
## Requirements

### General

- Allowed editors: vi, vim, emacs
- Execution environment: Ubuntu 18.04 LTS using Sass 3.7.4 (or higher)
- Files should end with a new line
- Scss files must have a comment at the beginning (i.e., syntax above)
- All files should start with a comment describing the task
- Mandatory README.md file at the root of the project folder

### Installation

```bash
$ sudo apt-get install -y ruby2.5 ruby2.5-dev
$ sudo apt-get install ubuntu-dev-tools
$ gem install sass -v 3.7.4
$ sass --version
```

## Project Structure

- All Sass/Scss files must start with a comment block.
- Files should end with a new line.
- Scss files should have a comment at the beginning describing the syntax.
- Each file should start with a comment describing the task.
- Include a README.md file at the root of the project.

## Quiz Questions

Make sure to validate all quiz questions before moving on to project tasks.

## Project Tasks

### Task 0: Always debugging!

Write a Sass file that prints "Hello world" in the debug output.

### Task 1: Color variable

Write a Sass file that assigns the text color #3D3D3D to the HTML tags `body` and `p`. Use a Sass variable.

### Task 2: Colors

Write a Sass file that assigns text color #3D3D3D to `body` and `p`, and background color #6D6D6D to `body` and `h2`. Use 2 Sass variables.

...

_(Continue with tasks 3 through 16)_

## Repository Information

- GitHub repository: [alx-frontend-for-fun](https://github.com/Dr-dyrane/alx-frontend-for-fun)
- Directory: sass_scss

## Copyright

Copyright © 2024 ALX, All rights reserved.
