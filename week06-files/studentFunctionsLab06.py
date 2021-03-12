# functionsLab.py
# This program creates and views students using functions
# Author: Alan Healy
# Date Created: 12-MAR-2021

import json

filename = "studentData.json"

def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj, f)

def readDict():
    with open(filename, 'r') as f:
        return json.load(f)

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(l) Load students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/s/l/q): ").strip()
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

def doSave(students):
    writeDict(students)
    print("Students have been saved.")

def doLoad():
    studentDict = readDict()
    print(studentDict)

# main function
students = []
choice = displayMenu()

while(choice != 'q'):

    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice == 's':
        doSave(students)
    elif choice == 'l':
        doLoad()
    elif choice != 'q':
        print("\nPlease select either a,v or q")
    
    choice = displayMenu()

