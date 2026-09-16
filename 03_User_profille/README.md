# Task 03 — User Profile

## 🎯 Project Goal

Build a command-line User Profile program in Python that collects basic information from a user, validates the input, stores the information in a dictionary, and displays a formatted profile.

The program focuses on practicing user input, validation, dictionaries, functions, and basic control flow.

---

## ✨ Features

* User name validation
* Age validation
* City input
* Programming language input
* Student status handling
* Input validation
* Exit commands
* Dictionary-based data storage
* Formatted profile output

---

## 🧠 Concepts Practiced

* Variables
* Strings
* Data Types
* Functions
* Type Hints
* `if / else`
* `while` loops
* Dictionaries
* `input()`
* String methods
* Type conversion
* Boolean logic
* `None`
* Input validation

---

## 📁 Project Structure

```text
03_user_profile/
├── user_profile.py
└── README.md
```

---

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python user_profile.py
```

---

## 💻 Example

### Input

```text
Name: Aida
Age: 20
City: Baku
Programming Language: Python
student status: yes
```

### Output

```text
====USER PROFILE====

Name: Aida
Age: 20
City: Baku
favorite language: Python
student: YES
```

---

## 🛡️ Input Validation

The program validates user input before creating the profile.

### Name

The name must contain alphabetic characters and spaces.

Invalid examples:

```text
Aida123
123
```

### Age

The age must be a valid integer.

Invalid example:

```text
Age: abc
```

The program asks the user to enter the value again.

### Student Status

The program handles student status input and converts the result into a consistent `YES` / `NO` representation.

---

## 🚪 Exit Commands

The program can be terminated during name input by entering:

```text
q
```

or:

```text
quit
```

or:

```text
exit
```

---

## 📦 Data Structure

User information is stored in a Python dictionary.

The profile contains:

```text
Name
Age
City
Favorite Language
Student Status
```

---

## ✅ Acceptance Criteria

* [x] User name is collected.
* [x] User age is collected.
* [x] City is collected.
* [x] Programming language is collected.
* [x] Student status is collected.
* [x] Invalid names are handled.
* [x] Invalid ages are handled.
* [x] User information is stored in a dictionary.
* [x] The profile is displayed in a readable format.
* [x] The program uses functions to separate responsibilities.
* [x] Type hints are used where appropriate.
* [x] The user can exit the program.

---

## 📚 What I Practiced

This task helped me practice collecting and validating different types of user input and organizing the resulting data using a Python dictionary.

I also practiced breaking a program into smaller functions instead of keeping all logic inside the `main()` function.

---

## 🚀 Status

**Completed — Python Intermediate**

Task 03 of 15
