# 1.6 Developing an Application Menu

from datetime import datetime
# This application displays a spreadsheet automation menu and processes a selected option.

# Print application header
print("EriBek9068's Spreadsheet Automation Menu")

print("Choose a number from the following options")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

# The next line retrieves the inputted option and stores into the variable called option.
option = input()

print("You selected", option, "at", str(datetime.now()))
