# studentFunction.py
# This program is for testing a function used in functionsLab.py
# Author: Alan Healy
# Date Created: 28-FEB-2021

students = []

def readModules():
    modules = []
    moduleName = input("\tEnter the first module name (blank to quit): ").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\t\tEnter grade: "))
        modules.append(module)

        moduleName = input("\tEnter next module name (blank to quit): ").strip()

    return modules

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("Enter name: ")
    currentStudent["modules"] = readModules()

    students.append(currentStudent)

# test

doAdd(students)

doAdd(students)

print(students)
print("-----")