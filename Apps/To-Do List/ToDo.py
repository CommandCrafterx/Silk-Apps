# This is a simple to-do list app that allows the user to add, delete, view, and save items to a list. By Silk OS.

import os

# Initialize an empty to-do list
todoList = []

# Function to create a new item in the to-do list
def createItem(item):
    todoList.append(item)
    print(f"\"{item}\" has been added to the list.")

# Function to delete an item from the to-do list
def deleteItem():
    print('''What Item would you like to delete?
          1. Last Item
          2. Custom Item''')
    userInput = input("> ")
    if userInput == '1':
        # Remove the last item in the list
        print(f"\"{todoList.pop()}\" has been removed from the list.")
    elif userInput == '2':
        # Remove a custom item specified by the user
        print("What item would you like to delete?")
        item = input("> ")
        if item in todoList:
            todoList.remove(item)
            print(f"\"{item}\" has been removed from the list.")
        else:
            print(f"\"{item}\" is not in the list.")
    else:
        print("Invalid input. Please try again.")

# Function to view all items in the to-do list
def viewList():
    if len(todoList) == 0:
        print("The list is empty.")
    else:
        print("Here is the list:")
        for item in todoList:
            print(f"- {item}")

# Function to save the to-do list to a file
def saveToFile():
    print("What would you like to name the file? (Do not include .txt)")
    name = input("> ") + ".txt"
    with open(name, "w") as file:
        for item in todoList:
            file.write(f"{item}\n")
    print(f"The list has been saved to {name}")

# Function to get valid input from the user
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

# Main function to run the to-do list app
def main():
    while True:
        userInput = getValidInput()
        if userInput == '1':
            print("What item would you like to add?")
            createItem(input("> "))
        elif userInput == '2':
            deleteItem()
        elif userInput == '3':
            viewList()
        elif userInput == '4':
            saveToFile()
        else:
            print("Do you want to quit? (y/n)")
            if input("> ") == 'y':
                print("Goodbye!")
                break

# Welcome message and credits, also starts the app
print()
print("Welcome to the To-Do List App!")
print("Credits: Silk OS Linux")
main()