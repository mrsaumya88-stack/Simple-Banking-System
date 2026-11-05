# 🏦 Simple Banking System

PS No.: 14
Project Title: Simple Banking System
Programming Language: Python 3
Institution: Rungta International Skills University
Department: School of Computer Science and Engineering
Course: Bachelor of Technology – Computer Science and Engineering

# Student Details
**ERP ID**Ru-26-02462
**Seletion**A2

# 📌 1. Project Overview

The Simple Banking System is a console-based banking application developed using Python 3. It allows customers to perform basic banking operations such as creating an account, depositing money, withdrawing money, transferring funds between accounts, and checking account balances.

The application uses Python programming concepts such as loops, functions, conditional statements, and file handling to provide a simple and user-friendly banking experience.

Account information is stored in a text file named bank.txt to maintain data between program executions.

# 🎯 2. Project Objectives

The main objectives of this project are:

To develop a simple banking application using Python 3.
To create bank accounts with unique account numbers.
To implement deposit and withdrawal operations.
To provide money transfer functionality between accounts.
To enable customers to check their account balances.
To maintain a minimum account balance of ₹500.
To validate user inputs and prevent invalid transactions.
To store and retrieve account information using file handling.
✨ 3. Features

# The application provides the following functionalities:

Account Creation: Create a new bank account with a unique account number.
Deposit Money: Deposit money into an existing bank account.
Withdraw Money: Withdraw money while maintaining the minimum balance requirement.
Money Transfer: Transfer funds from one existing account to another.
Balance Enquiry: Check the current balance of any existing account.
File Handling: Store and retrieve account information using bank.txt.
Input Validation: Handle invalid account numbers, incorrect amounts, and insufficient balances.
Menu-Driven Interface: Perform banking operations through a console-based menu.
# 🛠️ 4. Technologies and Concepts Used
Technology / Concept	Purpose
Python 3	Main programming language
Loops	Repeated menu operations
Functions	Separate banking operations
Conditional Statements	Decision-making and validation
File Handling	Saving and loading account information
Text File	Persistent account data storage
# 💻 5. System Requirements
Software Requirements
Python 3.x
Visual Studio Code / Python IDLE / Any Python-compatible IDE
Windows / Linux / macOS
Hardware Requirements
Laptop or desktop computer
Minimum 2 GB RAM
Basic available storage space
# 📂 6. Project Structure
text
Simple-Banking-System/
│
├── one.py
│
├── README.md
│
├── bank.txt
│
└── Screenshots.pdf

File Description
one.py – Main Python program containing the banking system.
README.md – Complete project documentation.
bank.txt – Stores account information and balances.
Screenshots.pdf – Contains screenshots of all four test cases showing their respective inputs and outputs.

Note: The bank.txt file should be created automatically by the program if it does not exist.

# ⚙️ 7. Installation and Execution

Follow these steps to execute the project.

Step 1: Install Python

Download and install Python 3 from the official website:

https://www.python.org/downloads/

Step 2: Clone the Repository

Open your terminal and execute:

bash
git clone YOUR_GITHUB_REPOSITORY_URL

Step 3: Open the Project Folder

Navigate to the downloaded project folder:

bash
cd Simple-Banking-System

Step 4: Execute the Python File

Run the following command:

bash
python one.py


Alternatively:

bash
python3 one.py

Step 5: Perform Banking Operations

Follow the menu displayed in the terminal and select the desired banking operation.

# ⌨️ 8. Input Details

The program accepts the following inputs:

Menu option for selecting a banking operation.
Customer name during account creation.
Initial deposit amount.
Account number for deposit operations.
Account number and withdrawal amount.
Source and destination account numbers for money transfers.
Transfer amount.
Account number for balance enquiry.
# 📤 9. Expected Output

The application displays appropriate messages for:

Successful account creation.
Account number and available balance.
Successful money deposits.
Successful money withdrawals.
Successful money transfers.
Updated account balances.
Account balance enquiries.
Invalid account numbers.
Insufficient balance.
Invalid transaction amounts.
Unsuccessful transactions.
# 💰 10. Banking Rules and Minimum Requirements

The following rules must be maintained:

The initial account number starts from 1001.
Each newly created account must have a unique account number.
The minimum account balance is ₹500.
Withdrawals must not reduce the balance below ₹500.
Transfers must not reduce the sender's balance below ₹500.
Deposits and transaction amounts must be valid and positive.
Money transfers are allowed only between existing accounts.
Account information must be stored and retrieved using file handling.
# 🧪 11. Test Cases and Expected Results

The following four test cases are taken from the official project assignment.

Test Case 1: Normal Input

Operation: Create Account

Input:

Menu Option: 1 (Create Account)
Name: Anil
Opening Deposit: 2000

Expected Output:

text
Account created.
A/C No: 1001
Balance: 2000


Expected Result: The account should be created successfully with account number 1001 and an opening balance of ₹2000.

Test Case 2: Boundary / Minimum Input

Operation: Withdraw Money

Input:

Account Number: 1001
Existing Balance: 2000
Withdrawal Amount: 1500

Expected Output:

text
Withdrawal successful.
Balance: 500


Expected Result: The withdrawal should be successful, and the remaining balance should be ₹500, which satisfies the minimum balance requirement.

Test Case 3: Invalid Input

Operation: Transfer Money

Input:

Account Number: 1001
Existing Balance: 2000
Transfer Amount: 100
Destination Account Number: 9999

Expected Output:

text
Account 9999 not found.
Transfer canceled.


Expected Result: The transfer should be canceled because destination account 9999 does not exist. The source account balance should remain unchanged.

Test Case 4: Different Valid Scenario

Operation: Transfer Money and Balance Enquiry

Input:

Account 1001: 2000
Account 1002: 3000
Transfer Amount: 1000
From Account: 1002
To Account: 1001
Balance Enquiry: 1001

Expected Output:

text
Transfer successful.
1002 balance: 2000
1001 balance: 3000


Expected Result: The transfer should be successful. Account 1002 should have ₹2000 remaining, while account 1001 should have ₹3000.

Important Testing Note: Each test case must be executed independently with the specified initial account balances. This ensures that previous transactions do not affect subsequent test results.

# 🛡️ 12. Error Handling and Input Validation

The system should handle the following situations:

Invalid menu selection.
Non-numeric input where a number is required.
Account number not found.
Negative or zero transaction amounts.
Insufficient account balance.
Minimum balance violation.
Invalid destination account number.
Invalid customer details.

Appropriate error messages should be displayed whenever an invalid operation is attempted.

# 💾 13. Data Storage and File Handling

The project uses a text file named bank.txt to store account information.

The program should:

Create the file if it does not already exist.
Save newly created account information.
Update account balances after successful transactions.
Load existing account information when the program starts.
Preserve account data between program executions.
# 📸 14. Screenshots and Testing Documentation

A PDF file named Screenshots.pdf must be included in the GitHub repository.

The PDF should contain clear screenshots of all four test cases.

Each screenshot must show:

Test case number.
Input entered into the program.
Corresponding output displayed by the program.
Successful transaction or expected error message.
Screenshot Requirements
Execute each test case individually.
Capture the input and corresponding output.
Ensure all text is clearly visible.
Save screenshots in the correct order.
Combine all screenshots into one PDF.
Verify that every page of the PDF is readable.
Upload the final PDF to GitHub.
# ✅ 15. Testing and Verification

The following testing activities must be completed before submission:

Verify successful account creation.
Verify deposit functionality.
Verify withdrawal functionality.
Verify minimum balance restrictions.
Verify money transfer functionality.
Verify invalid account handling.
Verify balance enquiry.
Verify data persistence using file handling.
Execute all four assignment test cases individually.
Compare actual outputs with expected outputs.

All specified test cases must pass before final submission.

🎓 16. Learning Outcomes

Through this project, we gain practical experience in:

Python programming fundamentals.
Function-based programming.
Loops and conditional statements.
File handling and data persistence.
Input validation and error handling.
Basic banking transaction logic.
Software testing and debugging.
Project documentation and GitHub usage.
# 📝 17. Conclusion

The Simple Banking System demonstrates the practical application of fundamental Python programming concepts in developing a basic banking application.

It provides essential banking functionalities, including account creation, money deposits, withdrawals, fund transfers, and balance enquiries.

The project also demonstrates the importance of input validation, minimum balance restrictions, file handling, and software testing.

Overall, this project helps strengthen programming and problem-solving skills through the development of a practical console-based application.

# 👨‍🏫 18. Project Mentor

Mentored by: Mr. Satyaprakash Sethy

GitHub: @SATYAPRAKASHSETHY

Role: Python Mentor / Technical Guide

Special thanks to Mr. Satyaprakash Sethy for his valuable guidance, mentorship, and technical support throughout this project.

GitHub Profile: https://github.com/SATYAPRAKASHSETHY

Project: Simple Banking System
PS Number: 14
Institution: Rungta International Skills University