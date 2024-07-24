def display_menu():
    print("\nContact Book Menu")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts in your contact book.")
    else:
        print("\nContacts:")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
    print(f"Contact '{name}' added successfully.")

def search_contact(contacts):
    name = input("Enter the name to search: ")
    if name in contacts:
        print(f"Found contact - Name: {name}, Phone: {contacts[name]}")
    else:
        print(f"No contact found with the name '{name}'.")

def delete_contact(contacts):
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"No contact found with the name '{name}'.")

def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting the contact book application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
