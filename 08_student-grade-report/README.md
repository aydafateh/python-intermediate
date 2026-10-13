# Student Grade Report

A simple Python console application that collects student names and grades, evaluates their academic performance, and generates a final report with statistical information.

## Features

- **Input Validation:** Validates the number of students, student names, and grades.
- **Grade Evaluation:** Assigns a performance status based on each student's grade.
- **Final Report:** Displays each student's name, grade, and status.
- **Statistical Analysis:** Calculates the average, highest, and lowest grades.
- **Student Statistics:** Counts successful and unsuccessful students.

## Grading System

| Grade Range | Status |
|---|---|
| 0 to less than 10 | Rejected |
| 10 to less than 15 | Accepted |
| 15 to less than 18 | Good |
| 18 to 20 | Excellent |

## Technologies Used

- Python 3
- Dictionaries
- Lists
- `while` and `for` loops
- Conditional statements
- Exception handling (`try/except`)
- Input validation
- Basic statistical calculations

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Clone the repository or download this project.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
python main.py
```

## Example

```text
enter the number of students: 3

=====student 1====
student name 1: Ali
student core 1: 18

=====student 2====
student name 2: Sara
student core 2: 15

=====student 3====
student name 3: Reza
student core 3: 8


===final report===

Ali : 18.0 --> excellent
Sara : 15.0 --> good
Reza : 8.0 --> rejected

number of student : 3
average grades : 13.666666666666666
highest score : 18.0
lowest score : 8.0

number of successful : 2
number of unsuccessful : 1
```

## Learning Objectives

This project was created to practice intermediate Python programming concepts, including data collection, input validation, dictionaries, loops, exception handling, and data analysis.

## Future Improvements

- Refactor the code into reusable functions.
- Handle duplicate student names.
- Format the average grade to two decimal places.
- Add support for saving reports to a file.

---

**Project:** Student Grade Report  
**Language:** Python