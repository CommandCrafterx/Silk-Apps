# This is a simple to-do list app that allows the user to add, delete, view, and save items to a list.

import os

# Initialize an empty to-do list
todoList = []
FILE_NAME = "to-do.txt"

# Function to create a new item in the to-do list
def createItem(item):
    todoList.append(item)
    print(f"\"{item}\" has been added to the list.")

# Function to delete an item from the to-do list
def deleteItem():
    print('''What Item would you like to delete?
          1. Last Item
          2. Custom Item''')
    userChoice = input("Enter your choice: ")

    if userChoice == "1":
        if todoList:
            removed = todoList.pop()
            print(f"\"{removed}\" has been removed from the list.")
        else:
            print("The list is empty.")
    elif userChoice == "2":
        itemToRemove = input("Enter the exact item to delete: ")
        if itemToRemove in todoList:
            todoList.remove(itemToRemove)
            print(f"\"{itemToRemove}\" has been removed from the list.")
        else:
            print("Item not found in the list.")
    else:
        print("Invalid choice.")

# Function to view the current to-do list
def viewList():
    if not todoList:
        print("The list is empty.")
    else:
        print("Your current to-do list:")
        for i, item in enumerate(todoList, start=1):
            print(f"{i}. {item}")

# Function to save the list to a file
def saveList():
    if os.path.exists(FILE_NAME):
        overwrite = input(f"The file '{FILE_NAME}' already exists. Overwrite? (Y/N): ").strip().lower()
        if overwrite != 'y':
            print("File was not overwritten.")
            return
    
    try:
        with open(FILE_NAME, 'w', encoding='utf-8') as file:
            file.writelines(f"{item}\n" for item in todoList)
        print(f"List saved to '{FILE_NAME}'.")
    except Exception as e:
        print(f"An error occurred while saving the list: {e}")

# Main menu loop
def main():
    while True:
        print('''\nTo-Do List Menu
        1. Add Item
        2. Delete Item
        3. View List
        4. Save List
        5. Exit''')
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to add: ")
            createItem(item)
        elif choice == "2":
            deleteItem()
        elif choice == "3":
            viewList()
        elif choice == "4":
            saveList()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
