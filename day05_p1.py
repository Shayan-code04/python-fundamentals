def contact_manager():
    print("\nWelcome to the Contact Manager!")

    contacts = {}

    while True:
        print("\n===== Contact Manager =====")
        print("1. Add Contact")
        print("2. Look Up Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            contacts[name] = phone
            print(f"{name} added successfully.")

        elif choice == "2":
            name = input("Enter contact name to search: ")
            phone = contacts.get(name)

            if phone:
                print(f"{name}'s phone number is {phone}")
            else:
                print("Contact not found.")

        elif choice == "3":
            name = input("Enter contact name to update: ")

            if name in contacts:
                new_phone = input("Enter new phone number: ")
                contacts[name] = new_phone
                print("Contact updated successfully.")
            else:
                print("Contact not found.")

        elif choice == "4":
            name = input("Enter contact name to delete: ")

            if name in contacts:
                del contacts[name]
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")

        elif choice == "5":
            print("Exiting Contact Manager...")
            break

        else:
            print("Invalid choice. Please try again.")
contact_manager()

