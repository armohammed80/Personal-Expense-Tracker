# Personal Expense Tracker Course-End Project 

## Overview
This Python script is designed to manage a personal expense tracker. It provides functionality to add expenses, view them, set and track a monthly budget, and write the data to a CSV file. The program makes use of multiple classes and libraries to handle data storage, validation, and presentation in a user-friendly manner.

## Key Libraries
-	**csv**: The DictReader and DictWriter classes are used to read from and write to CSV files in a dictionary format.
-	**prettytable**: This is used to neatly format and display the expenses in a table.
- **datetime**: Used for validating and filtering dates based on the current date.
-	**math**: The fabs function is used to calculate the absolute difference between budget and expenses in case the limit is exceeded.

## Constants
-	**DATA_FILE**: Defines the location of the CSV file where expenses are stored (data.csv).
-	**DATE_FORMAT**: Specifies the date format (YYYY-MM-DD) for the input and validation of expense dates.
-	**FIELDNAMES**: A list of the column headers for the CSV file: "Date", "Category", "Amount", and "Description".

## Classes
### Expense Class
The Expense class manages the expenses. It allows the user to load, add, view, and write expenses. The major functions within this class are:
1.	__init__: Initializes the class with the file location and loads the data from the file.
2.	load_data: Loads the data from the CSV file and returns it as a list of dictionaries, each representing a row in the file. If the file is not found, it creates a new one.
3.	write_data: Writes the expense data back to the CSV file, ensuring the data is saved in the correct format.
4.	add_expense: Allows the user to input new expense details (date, category, amount, and description) and adds it to the self.data list.
5.	prune_data: Removes any entries that have empty fields to maintain data integrity.
6.	view_expenses: Displays the expenses in a table format using PrettyTable. It prunes the data before displaying.
7.	is_valid_date: A static method that checks if a given date is valid according to the specified date format.

### Budget Class
The Budget class is responsible for tracking and comparing the total expenses for the current month against a predefined budget limit. Key functions:
1.	__init__: Initializes the class with a budget limit and filters the expense data to only include entries from the current month.
2.	track_budget: Calculates the total expenses for the current month, compares it to the budget limit, and provides feedback on whether the budget has been exceeded.
3.	filter: Filters the expense data to only include entries from the current month, based on the date.
4.	set_monthly_budget: Prompts the user to set a monthly budget and ensures the value is valid.

## Main Program Logic
The program starts by initializing an Expense object with the data file (data.csv). A loop is provided to show the user a menu with options:
1.	Add Expense: Calls the add_expense method to allow the user to input new expenses.
2.	View Expenses: Displays all current expenses in a tabular format using the view_expenses method.
3.	Input Monthly Budget: Prompts the user to set a monthly budget by calling the set_monthly_budget method.
4.	Track Budget: Compares total expenses for the current month to the set monthly budget, providing feedback if the budget is exceeded.
5.	Write to File: Writes the current expense data to the CSV file.
6.	Write to File & Exit: Writes data to the file and then exits the program.

## Data Flow
1.	When the user adds an expense, it is stored in memory in self.data and written to the CSV file.
2.	The program continually checks and prunes the data to remove any incomplete records (empty values).
3.	Expenses are filtered by the current month, ensuring that only the relevant entries are tracked when comparing with the monthly budget.

## User Interface
The user interacts with the program through a terminal or command-line interface. It provides clear prompts for input and feedback, ensuring that the user is guided through the process. The use of a table to view expenses makes the information more readable and accessible.
Error Handling
-	Invalid Date Input: The program ensures that the date entered by the user matches the expected format (YYYY-MM-DD).
-	Invalid Amount Input: The program prompts the user to re-enter the amount if it’s not a valid number.
-	Empty Data: The program removes any expenses that have missing or invalid data.

## Conclusion
This Python program serves as a simple but effective expense tracking tool, allowing users to log, view, and manage their expenses while staying within a defined budget. The use of classes for modularization makes the code easy to maintain and extend, and the integration of CSV file handling ensures that data persists between sessions.
