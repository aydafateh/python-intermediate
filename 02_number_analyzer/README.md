# Task 02 — Number Analyzer

## 🎯 Project Goal

Build a command-line Number Analyzer in Python that receives numbers from the user and analyzes each number based on its numerical properties.

The program identifies whether a number is positive, negative, or zero, determines whether it is even or odd, and keeps track of the maximum number entered by the user.

The program continues accepting numbers until the user chooses to exit.

---

## ✨ Features

* Number input validation
* Positive / Negative / Zero detection
* Even / Odd detection
* Maximum number detection
* Multiple number input
* User-controlled exit
* Invalid input handling
* Function-based program structure

---

## 🧠 Concepts Practiced

* Variables
* Data Types
* Functions
* Conditional Statements
* `while` loops
* `for` loops
* Lists
* Boolean Logic
* Modulo Operator `%`
* Type Conversion
* String Methods
* `None`
* `break`
* Input Validation

---

## 📁 Project Structure

```text
02_number_analyzer/
├── number_analyzer.py
└── README.md
```

---

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python number_analyzer.py
```

---

## 💻 Example

### Input

```text
number: 10
number: -5
number: 0
number: 17
number: q
```

### Output

```text
even: Yes
positive: Yes

even: No
positive: No

even: Yes
positive: Zero

even: No
positive: Yes

max: 17
```

The program can be terminated by entering:

```text
q
```

or:

```text
exit
```

or:

```text
quit
```

---

## 🛡️ Input Validation

The program validates the user's input before analyzing it.

Invalid numeric input is rejected, while the following commands can be used to exit:

```text
q
exit
quit
```

---

## 📊 Number Analysis

For each number, the program determines:

### Sign

```text
Positive
Negative
Zero
```

### Parity

```text
Even
Odd
```

After the user finishes entering numbers, the program displays the maximum value entered.

---

## ✅ Acceptance Criteria

* [x] Positive numbers are identified correctly.
* [x] Negative numbers are identified correctly.
* [x] Zero is handled as a separate case.
* [x] Even numbers are identified correctly.
* [x] Odd numbers are identified correctly.
* [x] Multiple numbers can be entered.
* [x] The maximum number is calculated correctly.
* [x] Invalid input is handled.
* [x] The user can exit the program.
* [x] `q`, `exit`, and `quit` can be used to exit.
* [x] The program uses functions to separate responsibilities.
* [x] The program handles an empty list safely.

---

## 📚 What I Practiced

This task helped me practice working with numerical data, conditions, loops, lists, functions, and input validation.

I also practiced separating validation and analysis logic into different functions instead of placing the entire program inside `main()`.

---

## 🚀 Status

**Completed — Python Intermediate**

Task 02 of 15
