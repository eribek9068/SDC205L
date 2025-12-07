from datetime import datetime


# Function to insert data into a CSV file
# Takes a file path and a comma-separated string, appends it to the file

def insertData(filePath, dataString):
    try:
        with open(filePath, "a") as file:   # append mode (creates file if missing)
            file.write(dataString + "\n")
        return True
    except Exception as e:
        print("Error writing to file:", e)
        return False

# Function to view contents of a CSV file
# Takes a file path and displays its contents
def viewData(filePath):
    try:
        print(f"You selected 2 at {datetime.now()}")
        print(f"The file {filePath}")
        with open(filePath, "r") as file:
            contents = file.read()
            print(contents)
    except Exception as e:
        print("Error reading file:", e)
        
# Function to collect input and perform conversions
# Stores converted data into ZooData.csv using insertData
def convertData(value, spreadsheetType):
    if spreadsheetType == "Temperature":
        return (value - 32) * 5/9
    elif spreadsheetType == "Weight":
        return value / 2.205
    elif spreadsheetType == "Rain":
        return value * 2.54
    else:
        return None


def getInput():
    spreadsheetType = input("Enter spreadsheet type (Temperature, Weight, Rain): ").strip()

    numEntries = int(input("How many entries are you inputting?\n "))

    for _ in range(numEntries):
        date = input("Enter a date:\n ")

        # Prompt based on spreadsheet type
        prompts = {
            "Temperature": "Enter the highest temp for the inputted date:\n",
            "Weight": "Enter the weight in pounds for the inputted date:\n",
            "Rain": "Enter the rain amount in inches for the inputted date:\n"
        }
        value = float(input(prompts.get(spreadsheetType, "Enter a value:\n")))

        # Call to convertData (COMMENT REQUIRED BY THE ASSIGNMENT)
        # Calling convertData(value, spreadsheetType) → returns converted numerical result
        converted = convertData(value, spreadsheetType)

        # Build CSV line
        dataLine = f"{date},{value},{converted}"

        # Try to save using insertData()
        if insertData("ZooData.csv", dataLine):
            print(f"The following data was saved at {datetime.now()}: {dataLine}")
        else:
            print("Error: Could not save entry.")


# Menu options

print("EriBek9068's Spreadsheet Automation Menu")
menuOptions = ["Input Data", "View Current Data", "Generate Report"]

print("Choose a number from the following options:")
for index, option in enumerate(menuOptions, start=1):
    print(f"{index} {option}")

userChoice = input()

# Menu flow control
if userChoice == "1":
    getInput()

elif userChoice == "2":
    viewData("ZooData.csv")

else:
    print("Error: The chosen functionality is not implemented yet")
