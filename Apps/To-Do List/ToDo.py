# This is a simple to-do list app that allows the user to add, delete, view, and save items to a list. By Silk OS.

import os

todoList = []

def createItem(item):
    todoList.append(input(item))
    print(f"\"{item}\" has been added to the list.")

def deleteItem():
    print('''What Item would you like to delete?
          1. Last Item
          2. Custom Item''')
    userInput = input("> ")
    if userInput == '1':
        print(f"\"{todoList.pop()}\" has been removed from the list.")
    elif userInput == '2':
        item = input("What item would you like to delete?")
        if item in todoList:
            todoList.remove(item)
            print(f"\"{item}\" has been removed from the list.")
        else:
            print(f"\"{item}\" is not in the list.")
    else:
        print("Invalid input. Please try again.")

def viewList():
    if len(todoList) == 0:
        print("The list is empty.")
    else:
        print("Here is the list:")
        for item in todoList:
            print(f"- {item}")

def saveToFile():
    print("What would you like to name the file? (Do not include .txt)")
    name = input("> ") + ".txt"
    with open(name, "w") as file:
        for item in todoList:
            file.write(f"{item}\n")
    print(f"The list has been saved to {name}.txt.")

def getValidInput():
    while True:
        print('''What do you want to do?
              1. Add an item
              2. Delete an item
              3. View the list
              4. Save to file
              5. Quit''')
        userInput = input("> ")
        if userInput in ['1', '2', '3', '4', '5']:
            return userInput
        else:
            print("Invalid input. Please try again.")

def main():
    while True:
        userInput = getValidInput()
        if userInput == '1':
            createItem(input("What item would you like to add? > "))
        elif userInput == '2':
            deleteItem()
        elif userInput == '3':
            viewList()
        elif userInput == '4':
            saveToFile()
        else:
            print("Goodbye!")
            break