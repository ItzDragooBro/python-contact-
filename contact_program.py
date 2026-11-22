contacts = {






    ok 
}

while True:
    

    print("==========Contact book==========")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    try:
    choice = int(input("Enter your choice (1-5): "))
    except ValueError:
    print("Please enter a number!")
    continue

    if choice == 1:
        name = input("Enter contact name: ")
        phone_no = int(input("Enter contact phone number: "))
        contacts[name] = phone_no
        print(f"Contact '{name}' added successfully.....!!!!")
    elif choice == 2:
        print("==========Contact List==========")
        if not contacts:
        print("No contacts found!")
        else:
        for name, phone in contacts.items():
        print(f"{name} : {phone}")

    elif choice ==3 :
        search_name = input("Enter contact name to search: ")
        if search_name in contacts:
            print(f"Contact is: {search_name} : {contacts[search_name]}")
        else:
            print("Contact not found, try adding some!!")
    elif choice == 4:
        delete_name = input("Enter contact name to delete: ")
        if delete_name in contacts:
            contacts.pop(delete_name)
            print(f"Contact '{delete_name}' deleted successfully.")
        else:
            print("Contact not found, try adding some!!")
    elif choice == 5:
        print("Exiting the program...")
        break
    else:

        print("Invalid choice. Please try again.")
