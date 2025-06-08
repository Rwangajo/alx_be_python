shopping_list = []

while True:
    print("\nMenu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f'"{item}" has been added to the shopping list.')

    elif choice == '2':
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f'"{item}" has been removed from the shopping list.')
        else:
            print(f'"{item}" was not found in the shopping list.')

    elif choice == '3':
        if shopping_list:
            print("Shopping List:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        else:
            print("Your shopping list is currently empty.")

    elif choice == '4':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
    
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            pass
        elif choice == '2':
            # Prompt for and remove an item
            pass
        elif choice == '3':
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
