import json

try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    contacts = {}

while True:

    print("\n========== Contact Book ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    if choice == 1:
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        with open("contacts.json", "w") as file:
            json.dump(contacts, file)
        print(f"Contact '{name}' added successfully!")
        
    elif choice == 2:
        print("\n========== Contact List ==========")
        if not contacts:
            print("No contacts found!")
        else:
            for name, phone in contacts.items():
                print(f"{name} : {phone}")

    elif choice == 3:
        search_name = input("Enter contact name to search: ")
        if search_name in contacts:
            print(f"{search_name} : {contacts[search_name]}")
        else:
            print("Contact not found!")

    elif choice == 4:
        delete_name = input("Enter contact name to delete: ")
        if delete_name in contacts:
            contacts.pop(delete_name)
            with open("contacts.json", "w") as file:
                json.dump(contacts, file)
            print(f"Contact '{delete_name}' deleted!")
        else:
            print("Contact not found!")

    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
