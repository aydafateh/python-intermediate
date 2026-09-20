# 🔐 Password Validator

A simple command-line Python program that validates the strength of a password based on a set of predefined requirements.

## 🎯 Project Goal

The goal of this project is to practice Python strings, loops, conditions, boolean variables, and string methods by creating a basic password strength validator.

A password is considered **Strong** when it satisfies all required conditions.

---

## ✨ Features

The program checks whether a password:

* Contains at least 8 characters
* Contains at least one digit
* Contains at least one lowercase letter
* Contains at least one uppercase letter

If all conditions are satisfied, the program displays:

```text
password: strong
```

Otherwise:

```text
password: not strong
```

---

## 🧠 Concepts Practiced

This project practices:

* `input()`
* Strings
* `len()`
* `for` loops
* `if / else`
* Boolean variables
* Boolean logic
* `and`
* `isdigit()`
* `islower()`
* `isupper()`
* Variable assignment
* Basic input validation

---

## 📁 Project Structure

```text
05_password_validator/
│
├── password_validator.py
└── README.md
```

---

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python password_validator.py
```

---

## 💻 Examples

### Strong Password

#### Input

```text
password Example: Aida1234
```

#### Output

```text
password: strong
```

### Weak Password — Too Short

#### Input

```text
password Example: Aida123
```

#### Output

```text
password : not strong
```

### Weak Password — No Uppercase

#### Input

```text
password Example: aida12345
```

#### Output

```text
password : not strong
```

### Weak Password — No Digit

#### Input

```text
password Example: AidaPassword
```

#### Output

```text
password : not strong
```

---

## 🔍 How It Works

The program starts by setting three Boolean variables to `False`:

```python
has_digit = False
has_lower = False
has_upper = False
```

It then checks whether the password has at least 8 characters.

If it does, the program loops through each character and checks:

* `isdigit()` → whether the character is a digit
* `islower()` → whether the character is lowercase
* `isupper()` → whether the character is uppercase

When each required type is found, its corresponding Boolean variable becomes `True`.

Finally, the program checks whether all required conditions are satisfied using `and`.

---

## ✅ Acceptance Criteria

* [x] Receive a password from the user
* [x] Check minimum password length
* [x] Check for at least one digit
* [x] Check for at least one lowercase character
* [x] Check for at least one uppercase character
* [x] Use Boolean variables to track requirements
* [x] Use a loop to inspect password characters
* [x] Use string validation methods
* [x] Use Boolean logic with `and`
* [x] Display whether the password is strong or not strong

---

## 📚 What I Practiced

This project helped me practice using loops and Boolean variables to track multiple conditions at the same time.

I also practiced Python string methods such as `isdigit()`, `islower()`, and `isupper()` and learned how to combine several conditions using Boolean logic.

---

## 📌 Status

**Completed ✅**

**Python Intermediate — Task 05 / 15**

**Project:** Password Validator
