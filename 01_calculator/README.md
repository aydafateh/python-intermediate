# Task 01 — Calculator

## 🎯 Project Goal

Build a command-line calculator in Python that accepts two numbers and an arithmetic operator, performs the selected operation, and displays the result.

The program also validates user input and handles division by zero safely.

## ✨ Features

* Addition
* Subtraction
* Multiplication
* Division
* Number validation
* Operator validation
* Division-by-zero handling
* Repeated calculations
* Modular function-based structure

## 🧠 Concepts Practiced

* Variables
* Data Types
* Functions
* Conditional Statements
* `while` loops
* User Input
* String Methods
* Exception Handling
* Boolean Logic
* Type Conversion
* Modules and Imports

## 📁 Project Structure

```text
01_basics/
├── calculator.py
├── validator.py
└── README.md
```

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python calculator.py
```

## 💻 Example

### Input

```text
first number: 20
operator: *
second number: 5
```

### Output

```text
result: 100
```

The calculator can also continue performing calculations:

```text
again?(y/n): y
```

## 🛡️ Input Validation

The program validates:

* Numeric input
* Supported arithmetic operators
* Division by zero

Supported operators:

```text
+
-
*
/
```

## ✅ Acceptance Criteria

* [x] Addition works correctly.
* [x] Subtraction works correctly.
* [x] Multiplication works correctly.
* [x] Division works correctly.
* [x] Division by zero is handled.
* [x] Invalid numbers are handled.
* [x] Invalid operators are handled.
* [x] The program supports repeated calculations.
* [x] The calculator is organized using functions.
* [x] Validation logic is separated into a dedicated module.

## 📚 What I Practiced

This task was designed to strengthen my understanding of Python fundamentals while practicing a more structured approach to writing programs.

The main focus was separating input validation, calculation logic, and program flow into independent functions.
