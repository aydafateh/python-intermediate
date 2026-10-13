# Banking System

A console-based banking application developed with Python to practice object-oriented programming, input validation, and transaction management.

## Features

- **User Information:** Collects and validates the user's name, phone number, and account number.
- **Check Balance:** Displays the current account balance.
- **Transfer Money:** Transfers money to another account, subject to available balance.
- **Deposit Money:** Adds money to the account balance.
- **Withdraw Money:** Withdraws money if sufficient funds are available.
- **Transaction History:** Displays recorded deposits, withdrawals, and transfers.
- **Change PIN:** Allows the user to change their account PIN after verifying the current PIN.
- **Input Validation:** Validates menu selections, amounts, PINs, and user information.

## Technologies and Concepts

- Python 3
- Object-Oriented Programming (OOP)
- Classes and Objects
- Dictionaries and Lists
- Instance Methods and Static Methods
- Input Validation
- Exception Handling (`try/except`)
- Loops and Conditional Statements
- Basic State Management

## Project Structure

The application is organized into five classes:

| Class | Responsibility |
|---|---|
| `Menus` | Defines the main menu and stores user information. |
| `Validator` | Validates user information and input values. |
| `Io` | Handles user input and input validation workflows. |
| `BankAccount` | Manages the balance, PIN, and transaction history. |
| `Application` | Coordinates the application and connects its components. |

## How to Run

1. Install Python 3.
2. Clone the repository or download the project.
3. Open a terminal in the project directory.
4. Run the application:

```bash
python main.py
```

## Default Settings

- Initial balance: `10000`
- Initial PIN: `1234`

These values are defined in the `BankAccount` class.

## Main Menu

1. Check Balance
2. Transfer Money
3. Deposit Money
4. Withdraw Money
5. Transaction History
6. User Information
7. Change PIN
8. Exit

## Learning Objectives

This project was created to practice organizing a Python application into separate classes, assigning responsibilities to each class, validating input, and managing account operations.

It also provides practice with methods, object initialization, instance attributes, and communication between objects.

## Future Improvements

- Prevent zero or negative transaction amounts.
- Validate account numbers consistently.
- Add PIN verification before sensitive operations.
- Prevent transfers to the same account.
- Improve transaction records with timestamps.
- Save account information and transactions to a file or database.
- Refactor the application into multiple Python modules.
- Add automated tests.

## Disclaimer

This is an educational project for practicing Python programming. It is not intended for real banking operations or handling actual financial information.