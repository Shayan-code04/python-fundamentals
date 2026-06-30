def inventory_management():
    """A simple inventory management system using a dictionary."""

    inventory = {}

    while True:
        print("\n===== Inventory Management =====")
        print("1. Add Item")
        print("2. View Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Show Full Inventory")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        # Add Item
        if choice == "1":
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item: "))

            inventory[item] = {
                "quantity": quantity,
                "price": price
            }

            print(f"{item} added successfully.")

        # View Item
        elif choice == "2":
            item = input("Enter item name to view: ")

            item_info = inventory.get(item)

            if item_info:
                total = item_info["quantity"] * item_info["price"]

                print("\nItem Details")
                print(f"Item     : {item}")
                print(f"Quantity : {item_info['quantity']}")
                print(f"Price    : {item_info['price']}")
                print(f"Total    : {total}")
            else:
                print("Item not found.")

        # Update Item
        elif choice == "3":
            item = input("Enter item name to update: ")

            if item in inventory:
                new_quantity = int(input("Enter new quantity: "))
                new_price = float(input("Enter new price: "))

                inventory[item]["quantity"] = new_quantity
                inventory[item]["price"] = new_price

                print("Item updated successfully.")
            else:
                print("Item not found.")

        # Delete Item
        elif choice == "4":
            item = input("Enter item name to delete: ")

            if item in inventory:
                del inventory[item]
                print("Item deleted successfully.")
            else:
                print("Item not found.")

        # Show Full Inventory
        elif choice == "5":
            if inventory:
                print("\n===== Inventory =====")

                for item, details in inventory.items():
                    total = details["quantity"] * details["price"]

                    print(f"\nItem     : {item}")
                    print(f"Quantity : {details['quantity']}")
                    print(f"Price    : {details['price']}")
                    print(f"Total    : {total}")
            else:
                print("Inventory is empty.")

        # Quit
        elif choice == "6":
            print("Thank you for using Inventory Management.")
            break

        # Invalid Choice
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


inventory_management()