inventory = {
    "Sugar": 10,
    "Rice": 25,
    "Salt": 15
}

# Menu loop
while True:
    print("\n=== Inventory Menu ===")
    print("1. View Inventory")
    print("2. Update Stock")
    print("3. Add New Item")
    print("4. Remove Item")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\nCurrent Inventory:")
        for item, quantity in inventory.items():
            print(f"- {item}: {quantity} units")

    elif choice == "2":
        item = input("Enter the item name to update: ").capitalize()
        if item in inventory:
            new_qty = int(input(f"Enter new quantity for {item}: "))
            inventory[item] = new_qty
            print(f"{item} updated to {new_qty} units.")
        else:
            print(f"{item} not found in inventory.")

    elif choice == "3":
        item = input("Enter the name of the new item: ").capitalize()
        if item in inventory:
            print(f"{item} already exists. Use option 2 to update it.")
        else:
            qty = int(input(f"Enter quantity for {item}: "))
            inventory[item] = qty
            print(f"{item} added with {qty} units.")

    elif choice == "4":
        item = input("Enter the item name to remove: ").capitalize()
        if item in inventory:
            del inventory[item]
            print(f"{item} has been removed.")
        else:
            print(f"{item} not found in inventory.")

    elif choice == "5":
        print("Exiting Inventory Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
