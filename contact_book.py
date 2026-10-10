"""
=============================================================================
Project Name : Command-Line Contact Book
Task Level   : Task 10, Level 1, Day 10 (Python Internship)
Description  : A beginner-friendly, menu-driven CLI Contact Book that stores,
               searches, updates, deletes, and views contacts using Python
               dictionaries (including nested dictionaries).
=============================================================================
"""

def is_valid_phone(phone: str) -> bool:
    """
    Helper function to validate a phone number.
    Rule: Must contain only digits and be exactly 10 digits long.
    """
    return phone.isdigit() and len(phone) == 10


def add_contact(contacts: dict) -> None:
    """
    Adds a new contact to the contact book.
    - Validates phone number (digits only, 10 digits).
    - Checks for duplicate phone numbers to prevent accidental overwriting.
    - Ensures the contact name is not empty.
    """
    print("\n--- ADD NEW CONTACT ---")

    # 1. Input and validate phone number
    phone = input("Enter 10-digit phone number: ").strip()

    if not is_valid_phone(phone):
        print(" Error: Invalid phone number! It must contain exactly 10 digits (numbers only).")
        return

    # Check for duplicate phone number using the 'in' keyword
    if phone in contacts:
        print(f" Error: A contact with phone number '{phone}' already exists ({contacts[phone]['name']}).")
        return

    # 2. Input and validate contact name
    name = input("Enter contact name: ").strip()
    if not name:
        print(" Error: Contact name cannot be blank!")
        return

    # 3. Input email and address (optional, can be empty or provided)
    email = input("Enter email address: ").strip()
    address = input("Enter physical address: ").strip()

    # Default placeholder text if user leaves email or address empty
    if not email:
        email = "N/A"
    if not address:
        address = "N/A"

    # 4. Store in the contacts dictionary as a nested dictionary
    # The phone number is the primary KEY, and the details are stored in the nested dictionary VALUE.
    contacts[phone] = {
        "name": name,
        "email": email,
        "address": address
    }

    print(f" Success: Contact '{name}' added successfully!")


def search_contact(contacts: dict) -> None:
    """
    Searches for a contact either by:
    1. Phone number (direct dictionary lookup using .get())
    2. Name (case-insensitive search iterating through dictionary values)
    """
    print("\n--- SEARCH CONTACT ---")
    if not contacts:
        print("ℹ Notice: The contact book is currently empty.")
        return

    print("1. Search by Phone Number")
    print("2. Search by Name")
    search_choice = input("Enter your search option (1 or 2): ").strip()

    if search_choice == "1":
        phone_query = input("Enter 10-digit phone number to search: ").strip()

        # Using .get() avoids a KeyError crash if the key does not exist.
        contact = contacts.get(phone_query)

        if contact is not None:
            print("\n Contact Found:")
            print("-" * 40)
            print(f"Phone Number : {phone_query}")
            print(f"Name         : {contact['name']}")
            print(f"Email        : {contact['email']}")
            print(f"Address      : {contact['address']}")
            print("-" * 40)
        else:
            print(f" No contact found with phone number '{phone_query}'.")

    elif search_choice == "2":
        name_query = input("Enter name (or part of name) to search: ").strip().lower()

        if not name_query:
            print(" Error: Search query cannot be empty.")
            return

        # Iterate through dictionary to find matching names
        matches = []
        for phone, details in contacts.items():
            if name_query in details["name"].lower():
                matches.append((phone, details))

        if matches:
            print(f"\n Found {len(matches)} matching contact(s):")
            print("=" * 60)
            for phone, details in matches:
                print(f"Phone Number : {phone}")
                print(f"Name         : {details['name']}")
                print(f"Email        : {details['email']}")
                print(f"Address      : {details['address']}")
                print("-" * 60)
        else:
            print(f" No contact found matching the name '{name_query}'.")

    else:
        print(" Error: Invalid search option! Please select 1 or 2.")


def update_contact(contacts: dict) -> None:
    """
    Updates existing contact details for a given phone number.
    Gracefully checks if the key exists before attempting update.
    Allows user to press Enter to keep existing values.
    """
    print("\n--- UPDATE CONTACT ---")
    if not contacts:
        print("ℹ Notice: The contact book is currently empty.")
        return

    phone = input("Enter the 10-digit phone number of the contact to update: ").strip()

    # Safe check using 'in' keyword to prevent KeyError
    if phone not in contacts:
        print(f" Error: No contact found with phone number '{phone}'.")
        return

    # Retrieve existing details
    current = contacts[phone]
    print(f"\nCurrent details for {phone}:")
    print(f"Name   : {current['name']}")
    print(f"Email  : {current['email']}")
    print(f"Address: {current['address']}")
    print("\n(Tip: Press Enter without typing anything to keep the current value)")

    # 1. Update Name
    new_name = input(f"Enter new name [{current['name']}]: ").strip()
    if not new_name:
        new_name = current['name']

    # 2. Update Email
    new_email = input(f"Enter new email [{current['email']}]: ").strip()
    if not new_email:
        new_email = current['email']

    # 3. Update Address
    new_address = input(f"Enter new address [{current['address']}]: ").strip()
    if not new_address:
        new_address = current['address']

    # Apply the updates
    contacts[phone]["name"] = new_name
    contacts[phone]["email"] = new_email
    contacts[phone]["address"] = new_address

    print(f" Success: Contact for '{phone}' updated successfully!")


def delete_contact(contacts: dict) -> None:
    """
    Deletes a contact from the dictionary using the phone number.
    Safely checks existence first, asks for confirmation, then removes the item.
    """
    print("\n--- DELETE CONTACT ---")
    if not contacts:
        print("ℹ Notice: The contact book is currently empty.")
        return

    phone = input("Enter the 10-digit phone number to delete: ").strip()

    # Graceful check with .get() - returns None if key does not exist
    contact = contacts.get(phone)
    if contact is None:
        print(f" Error: No contact found with phone number '{phone}'.")
        return

    # Prompt user for confirmation before deleting
    confirm = input(f"Are you sure you want to delete '{contact['name']}' ({phone})? (y/n): ").strip().lower()
    if confirm == "y":
        # Remove the key-value pair from the dictionary
        del contacts[phone]
        print(f" Success: Contact '{contact['name']}' ({phone}) has been deleted.")
    else:
        print(" Deletion cancelled.")


def view_contacts(contacts: dict) -> None:
    """
    Displays all stored contacts in a clean, tabular format.
    Handles the empty state gracefully.
    """
    print("\n--- ALL CONTACTS ---")
    if not contacts:
        print("ℹ Notice: No contacts found in the contact book.")
        return

    print(f"Total Contacts: {len(contacts)}")
    print("=" * 85)
    print(f"{'Phone Number':<15} | {'Name':<22} | {'Email':<25} | {'Address'}")
    print("=" * 85)

    # Iterate through all key-value pairs in the contacts dictionary
    for phone, details in contacts.items():
        name = details.get("name", "N/A")
        email = details.get("email", "N/A")
        address = details.get("address", "N/A")
        print(f"{phone:<15} | {name:<22} | {email:<25} | {address}")

    print("=" * 85)


def display_menu() -> None:
    """
    Prints the user menu with clear options.
    """
    print("\n" + "=" * 35)
    print("       CONTACT BOOK MENU")
    print("=" * 35)
    print(" 1. Add contact")
    print(" 2. Search contact")
    print(" 3. Update contact")
    print(" 4. Delete contact")
    print(" 5. View all contacts")
    print(" 6. Exit")
    print("=" * 35)


def main() -> None:
    """
    Main application controller:
    - Pre-loads 4 sample contacts.
    - Runs a while loop presenting the menu until the user selects Exit.
    - Validates menu inputs.
    """
    # Pre-loaded contacts dictionary (4 sample contacts)
    # Key: 10-digit Phone Number (string)
    # Value: Nested dictionary containing name, email, address
    contacts = {
        "9876543210": {
            "name": "Alice Johnson",
            "email": "alice@example.com",
            "address": "123 Maple Street, Springfield"
        },
        "9123456780": {
            "name": "Bob Smith",
            "email": "bob@example.com",
            "address": "456 Oak Avenue, Metropolis"
        },
        "9988776655": {
            "name": "Charlie Brown",
            "email": "charlie@example.com",
            "address": "789 Pine Road, Gotham"
        },
        "9845123456": {
            "name": "Diana Prince",
            "email": "diana@example.com",
            "address": "321 Cedar Lane, Star City"
        }
    }

    print("Welcome to Python CLI Contact Book!")
    print(f"Loaded {len(contacts)} sample contacts.")

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            view_contacts(contacts)
        elif choice == "6":
            print("\n Thank you for using Contact Book. Goodbye!\n")
            break
        else:
            print(" Error: Invalid menu choice! Please enter a number between 1 and 6.")


# Standard Python boilerplate to ensure main() runs only when executed directly
if __name__ == "__main__":
    main()
