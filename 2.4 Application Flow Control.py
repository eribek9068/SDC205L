# 1.6 Developing an Application Menu

from datetime import datetime
# This application displays a spreadsheet automation menu and processes a selected option.

# Print application header
print("EriBek9068's Spreadsheet Automation Menu")

# Menu options
menuOptions = [
    "Input Data",
    "View Current Data",
    "Generate Report"
]

# Display menu using a for-loop
print("Choose a number from the following options")
for index, option in enumerate(menuOptions, start=1):
    print(f'{index} {option}')

# Get user input
userChoice = input()

# Decision structure to validate input
if userChoice in ["1", "2", "3"]:
    selectedOption = menuOptions[int(userChoice) -1]
    print(f'You selected {userChoice} at {datetime.now()}')
else:
    print("Error: invalid choice selected")
