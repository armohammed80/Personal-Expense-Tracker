# Imports for this project, check requirements.txt for installing dependencies.
from csv import DictReader, DictWriter
from prettytable import PrettyTable
from datetime import datetime
from math import fabs

# Constants: These constants define where the path of the data file and the date format used.
DATA_FILE = "data.csv"
DATE_FORMAT = "%Y-%m-%d"
FIELDNAMES = ["Date", "Category", "Amount", "Description"]


class Expense:
    def __init__(self, file):
        """
        Handles expenses. Loads expenses from file, write to file, add expense and show all expenses in table format.

        Usage:
        >>> expense_tracker = Expense(file="data.csv")
        :param file:
        """
        self.file = file
        self.data = self.load_data()

    def load_data(self):
        """
        Returns data from the CSV file.
        :return:
        """
        # Opens the file in reading mode as 'file'
        try:
            with open(self.file, 'r') as file:
                # Uses the csv module to read the file as a dictionary.
                # Dictionary format: row_n = {column_1: value_1, ..., column_n: value_n}
                reader = DictReader(file)

                # Returns a list containing each row as a dictionary in the format of a list-comprehension.
                return [row for row in reader]
        except FileNotFoundError:
            file = open(self.file, 'x')
            file.close()
            return []

    def write_data(self):
        """
        Writes data in the 'self.data' variable to the file.
        :return:
        """
        # Opens the file in write-mode, newline is set to an empty string according to documentation.
        with open(self.file, 'w', newline='') as file:
            # Initializes the DictWriter class from csv module, takes input a list of dictionaries to write to CSV file.
            writer = DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(self.data)

    def add_expense(self):
        """
        Adds an expense data to the 'self.data'.
        :return:
        """
        print("\n---Adding Expense---")
        # Warning to user that invalid entries will not be viewed.
        print("NOTE: If any field is empty or invalid, it will not be viewed.")

        # Takes in date
        date = input("Date (YYYY-MM-DD): ")
        while not self.is_valid_date(date, DATE_FORMAT):
            # Continues asking for date untill it is valid.
            print("Invalid date input.")
            date = input("Date (YYYY-MM-DD): ")

        # Asks for categories.
        category = input("Category (Food, Travel, etc.): ")

        # Asks for amount untill it is valid.
        try:
            amount = float(input("Amount: $"))
        except ValueError:
            while True:
                try:
                    print("Invalid input for amount.")
                    amount = float(input("Amount: $"))
                    break
                except ValueError:
                    pass

        # Asks for description
        description = input("Short Description: ")

        # Adds this to the data.
        self.data.append({"Date": date, "Category": category, "Amount": amount, "Description": description})

    def prune_data(self):
        """
        Prunes all data row from 'self.data' with any empty values.
        :return:
        """
        # Iterates over each row by turning 'self.data' to a tuple so we don't run into any errors where deleting while
        # iterating.
        for row in list(self.data):
            # Iterates over each value in the row dict.
            for val in row.values():
                # If any value is an empty string, deleting it from 'self.data' and break loop to avoid double-deleting.
                if val == "":
                    self.data.remove(row)
                    break

    def view_expenses(self):
        """
        Prints the table using the package PrettyTable.
        :return:
        """
        # Prunes data.
        self.prune_data()

        # Configuring PrettyTable
        table = PrettyTable()
        table.align = "l"
        table.field_names = FIELDNAMES

        # Adds the values of each row from 'self.data' by using PrettyTable.add_rows() method.
        table.add_rows(list(row.values()) for row in self.data)

        # Finally, printing the table.
        print("\n---Expenses---")
        print(table)

    @staticmethod
    def is_valid_date(date_string: str, date_format: str):
        """
        Static method where it takes a date string and format and returns a boolean value to show if date is valid.
        :param date_string:
        :param date_format:
        :return (bool) is valid:
        """
        try:
            # Tries to turn the date string into a date instance using date format.
            datetime.strptime(date_string, date_format)

            # If passed, date is valid.
            return True
        except ValueError:
            # If failed, date is not valid.
            return False


class Budget:
    def __init__(self, limit: float, expenses: Expense):
        """
        Budget uses the data of the current month and uses a limit.
        :param limit:
        :param expenses:
        """
        self.limit = limit
        self.data = self.filter(expenses.data)

    def track_budget(self):
        """
        Tracks the budget by getting the total expenditure of current month and compares with the limit.
        :return:
        """
        # Tots up all the expenditure in the 'self.data'
        total = sum(float(row["Amount"]) for row in self.data)

        # Prints total expenditure.
        print(f"Total Amount: {total}")

        # Determines how much is left.
        if (left := self.limit - total) < 0:
            # If left is less than 0 (negative), then limit has been exceeded, print how much has exceeded.
            print(f"WARNING: You have exceeded your budget by {fabs(left):.2f}.")
        else:
            # Otherwise, print the amount left.
            print(f"You have ${left:.2f} left for the month.")

    @staticmethod
    def filter(data):
        """
        This static method filters data for the data in the current month.
        :param data:
        :return:
        """
        # Getting the current timestamp.
        now = datetime.now()

        # Filtering data
        filtered_data = []
        for row in data:
            # Checking if year and month of each row is that of current timestamp (Date is the current month).
            if now.month == datetime.strptime(row["Date"], DATE_FORMAT).month \
               and now.year == datetime.strptime(row["Date"], DATE_FORMAT).year:
                # If it is, then add to 'filtered_data'
                filtered_data.append(row)
        return filtered_data

    @staticmethod
    def set_monthly_budget():
        """
        Try getting a monthly budget until it is valid.
        :return:
        """
        while True:
            try:
                monthly_budget = float(input("Enter your monthly budget: "))
                if monthly_budget <= 0:
                    print("Budget must be a positive number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        print(f"Your monthly budget is set to {monthly_budget:.2f}.")
        return monthly_budget


# Main program.
def main():
    # Initialize Expense and monthly budget.
    expenses = Expense(file=DATA_FILE)
    monthly_budget = None

    # Menu loop.
    while True:
        # Print options:
        print("Options: ")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Input monthly budget")
        print("4. Track Budget")
        print("5. Write to file")
        print("6. Write to file & Exit")

        # Try getting UI until is valid (i.e an numerical).
        while True:
            try:
                user_input = int(input("Enter Option: "))
                break
            except ValueError:
                pass

        # Doing action based on UI using a match-case statement.
        match user_input:
            # Add expense
            case 1:
                expenses.add_expense()
            # View all expenses
            case 2:
                expenses.view_expenses()
            # Set monthly budget.
            case 3:
                monthly_budget = Budget.set_monthly_budget()
            # Track expenses.
            case 4:
                # Checking if monthly budget is set
                if monthly_budget is not None:
                    budget_tracker = Budget(monthly_budget, expenses)
                    budget_tracker.track_budget()
                else:
                    # If not, tell user to set monthly budget.
                    print("You must enter monthly budget. (Option 3)")
            # Write data to file.
            case 5:
                expenses.write_data()
            # Write data and exit.
            case 6:
                expenses.write_data()
                break
        print("--------------------------")
    print("------------------------------")

# Run program (main function) only if this script is executed.
if __name__ == "__main__":
    main()
