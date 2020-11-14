# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030, Created started script
# T.Ward, 11/17/20, Added code to complete Assignment 5
# ------------------------------------------------------------------------ #

# ----------- Data ------------- #
# Declare variables and constants
# First declare an object that represents a file.
strFile = "C:\\Users\\ld693a\\Desktop\\_PythonClass\\Mod05\\Assignment05\\ToDoList.txt"
objFile = None   # TW added objFile variable
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = "" # A Capture the user option selection
newTask = "" # TW added variable for user input
newPriority = "" # TW added variable for user input
delTask = "" # TW added variable for user input

# ------------ Processing -------- #
# Step 1 - When the program starts, load the any data you have into a text file called ToDoList.txt and into a
# python list of dictionaries rows.

objFile = open(strFile, "r")
for row in objFile:
    strData = row.split("|")
    dicRow = {"Task":strData[0].strip(),"Priority":strData[1].strip()}
    lstTable.append(dicRow)
    # print(dicRow) # TW - Uncomment this line to check that data is read in accurately from file.
objFile.close()

# ----------- Input/Output -------- #
# Step 2 - Display a menu of choices to the user

while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # Add a new line for neatness.
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'): # Strip() is used throughout to remove unwanted spaces, carriage returns from the entry.
        print("Task" + " | " + "Value")
        for row in lstTable:
            print(row["Task"] + " | " + row["Priority"])
        continue

    # Step 4 - Add a new item to the list table.  Convert to lower case.
    elif (strChoice.strip() == '2'):
        newTask = str(input('Please enter a new task: ')).lower()
        newPriority = str(input('Please enter the priority: ')).lower()
        dicRow = {"Task": newTask, "Priority": newPriority}
        lstTable.append(dicRow)
        # print(dicRow) # TW - Uncomment this line to check that data is entered accurately.
        continue

    # Step 5 - Remove a new item from the list table.  Convert to lower case.
    elif (strChoice.strip() == '3'):
        delTask = input('Please enter the task to delete: ')
        delTask = delTask.lower()
        i = 0  # Declare and initialize variable.  This will used a flag for telling the user the item does not exist.
        for row in lstTable:
            if delTask.strip() in row["Task"]:
                print("Now deleting forever and ever: " + delTask)
                lstTable.remove(row)
                i = i + 1 # If true, the script makes this a non-zero value.
        if i == 0: print("Task is not listed. Try again.")  # If i == 0, then the item was not found.  Tell the user.
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")  # The script will create the file, if it does not exist.
        print("Now saving data!")
        for row in lstTable:
            objFile.write(row["Task"] + " | " + row["Priority"] + '\n')
        objFile.close()
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program
