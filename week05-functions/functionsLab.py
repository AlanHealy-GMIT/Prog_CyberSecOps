# functionsLab.py
# This program creates and views students using functions
# Author: Alan Healy
# Date Created: 28-FEB-2021

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()
    choice = choice.lower()
    # print("You chose {}".format(choice))

    return choice


def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("Enter name: ")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)


def readModules():
    modules = []
    moduleName = input(
        "\tEnter the first module name (blank to quit): ").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\t\tEnter grade: "))
        modules.append(module)
        # read next module
        moduleName = input(
            "\tEnter next module name (blank to quit): ").strip()

    return modules

def displayModules(modules):
    print("\tName \t\tGrade")
    print("------------------")

    for module in modules:
        print("\t{} \t{}".format(module["name"], module["grade"]))

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])


# main function
students = []
choice = displayMenu()

while(choice != 'q'):

    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice != 'q':
        print("\nPlease select either a,v or q")
    
    choice = displayMenu()

