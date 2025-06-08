shopping_list = []

while True:
    print("\nMenu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item = input("Enter the item name to add: ")
        shopping_list.append(item)
        print(f'"{item}" has been added to the shopping list.')

    elif choice == '2':
        item = input("Enter the item name to remove: ")
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
