# 📝 Text Analyzer

A simple command-line Python program that analyzes a sentence and provides basic statistics about its content.

## 🎯 Project Goal

The goal of this project is to practice Python string manipulation, functions, loops, conditions, and dictionaries by building a simple text analyzer.

The program receives a sentence from the user and analyzes:

* Number of characters
* Number of words
* Number of uppercase characters
* Number of lowercase characters
* Number of digits
* Number of spaces

---

## ✨ Features

* Accepts text input from the user
* Validates the input
* Counts characters without spaces
* Counts words
* Counts uppercase characters
* Counts lowercase characters
* Counts digits
* Counts spaces
* Displays the results in a readable format

---

## 🧠 Concepts Practiced

This project practices the following Python concepts:

* Functions
* Function parameters
* Return values
* `while` loops
* `for` loops
* `if / else`
* Strings
* String methods
* `split()`
* `replace()`
* `count()`
* `len()`
* `isupper()`
* `islower()`
* `isdigit()`
* Dictionaries
* f-strings
* Input validation

---

## 📁 Project Structure

```text
04_text_analyzer/
│
├── text_analyzer.py
└── README.md
```

---

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python text_analyzer.py
```

---

## 💻 Example

### Input

```text
text: Hello World 123
```

### Output

```text
characters: 11
words: 3
uppercase_characters: 2
lowercase_characters: 8
digits: 3
spaces: 2
```

---

## 🔍 How It Works

The program first receives a sentence from the user.

It then passes the sentence to separate functions, with each function responsible for one part of the analysis.

For example:

* `character()` → counts characters
* `count_word()` → counts words
* `uppercase()` → counts uppercase characters
* `lowercase()` → counts lowercase characters
* `digit()` → counts digits
* `space()` → counts spaces

The results are stored in a dictionary and displayed to the user.

---

## ✅ Acceptance Criteria

* [x] Receive text from the user
* [x] Validate the input
* [x] Count characters
* [x] Count words
* [x] Count uppercase characters
* [x] Count lowercase characters
* [x] Count digits
* [x] Count spaces
* [x] Use functions for different operations
* [x] Store results in a dictionary
* [x] Display results clearly
* [x] Handle invalid text input

---

## 📚 What I Practiced

This project helped me practice working with strings and breaking a larger problem into smaller reusable functions.

It also reinforced the use of loops, conditions, string methods, dictionaries, and input validation in a practical Python program.

---

## 📌 Status

**Completed ✅**

**Python Intermediate — Task 04 / 15**

**Project:** Text Analyzer
