from datetime import datetime

# Print application header
print("EriBek9068's Spreadsheet Automation Menu")

# Menu options
menuOptions = [
    "Input Data",
    "View Current Data",
    "Generate Report"
]

# Display menu using a for-loop
print("Choose a number from the following options:")
for index, option in enumerate(menuOptions, start=1):
    print(f"{index} {option}")

# Get user input
userChoice = input()

# Decision structure to validate input
if userChoice in ["1", "2", "3"]:
    selectedOption = menuOptions[int(userChoice) - 1]
    print(f"You selected {userChoice} at {datetime.now()}")
else:
    print("Error: invalid choice selected")

# Function to convert data based on spreadsheet type
def convertData(value, spreadsheetType):
    if spreadsheetType == "Temperature":
        return (value - 32) * 5 / 9  # Fahrenheit to Celsius
    elif spreadsheetType == "Weight":
        return value / 2.205  # Pounds to Kilograms
    elif spreadsheetType == "Rain":
        return value * 2.54  # Inches to Centimeters
    else:
        return None

# Function to collect input and perform conversions
def getInput():
    spreadsheetType = input("Enter spreadsheet type (Temperature, Weight, Rain Amount): ").strip()
    numEntries = int(input("How many entries are you inputting?\n "))

    for _ in range(numEntries):
        date = input("Enter a date:\n ")
        valuePrompt = {
            "Temperature": "Enter the highest temp for the inputted date:\n",
            "Weight": "Enter the weight in pounds for the inputted date:\n",
            "Rain": "Enter the rain amount in inches for the inputted date:\n"
        }.get(spreadsheetType, "Enter a value:")

        value = float(input(valuePrompt))

        # Call convertData() with value and spreadsheetType, expecting a converted numerical result
        converted = convertData(value, spreadsheetType)

        print(f"The following was saved at {datetime.now()} :")
        print(f"{date},{value},{converted}")

# Call getInput() if user selected option 1
if userChoice == "1":
    getInput()
elif userChoice in ["2", "3"]:
    print("Error: The chosen functionality is not implemented yet")
