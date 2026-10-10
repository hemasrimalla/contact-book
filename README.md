# Command-Line Contact Book (Python)

> **Python Internship - Task 10 | Level 1 | Day 10**  
> A beginner-friendly, menu-driven CLI Contact Book built strictly using Python standard libraries and dictionary data structures.

---

## 📖 Project Overview

This project is an interactive terminal application designed to manage personal contacts. It demonstrates how to store, retrieve, update, and delete structured data using **Python dictionaries** (including **nested dictionaries**) while enforcing strict validation rules and graceful error handling.

The phone number serves as the primary unique key, mapping to a nested dictionary containing the contact's name, email, and physical address.

---

## ✨ Features

- **Menu-Driven Interface**: Clean, numbered menu running continuously in a `while` loop until the user chooses to exit.
- **Nested Dictionary Storage**: Contacts are indexed by a 10-digit phone number as the primary key:
  ```python
  contacts = {
      "9876543210": {
          "name": "Alice Johnson",
          "email": "alice@example.com",
          "address": "123 Maple Street, Springfield"
      }
  }
  ```
- **Robust Input Validation**:
  - Validates that phone numbers contain **digits only** and are **exactly 10 digits**.
  - Prevents **duplicate phone numbers** when adding a new contact.
  - Rejects **empty/blank names**.
  - Handles **invalid menu choices** gracefully without crashing.
- **Flexible Search**:
  - Search by 10-digit phone number (direct \(O(1)\) lookup).
  - Search by name or partial name (case-insensitive substring match).
- **Safe Update & Delete**:
  - Update allows pressing <kbd>Enter</kbd> to keep existing details.
  - Delete prompts for confirmation (`y/n`) before removing the contact.
- **Pre-loaded Data**: Comes with 4 realistic sample contacts so the program is immediately usable.
- **Modular Code**: Cleanly organized into dedicated functions (`add_contact`, `search_contact`, `update_contact`, `delete_contact`, `view_contacts`, `display_menu`, `main`) guarded by `if __name__ == "__main__":`.

---

## 🧠 Python Dictionary Concepts for Interviews

Here are essential interview talking points to explain the core concepts implemented in this project:

### 1. What is a Dictionary in Python?
A **dictionary** (`dict`) is an unordered (insertion-ordered in Python 3.7+), mutable collection of key-value pairs. Unlike lists or tuples which are indexed by sequential numeric positions (`0, 1, 2, ...`), dictionaries are indexed by **keys**, which must be of an immutable, hashable type (such as strings, integers, or tuples).
- **Time Complexity**: Dictionaries use an underlying hash table, providing an average lookup, insertion, and deletion time complexity of **\(O(1)\)** (constant time).

### 2. What is a Key-Value Pair?
A **key-value pair** is an association between a unique identifier (the key) and the data associated with it (the value).
- **Key**: Must be unique and hashable. In this project, the **10-digit phone number** is the key because phone numbers are globally unique to individuals.
- **Value**: Can be any Python object. In this project, the value is another dictionary (a **nested dictionary**) storing the user's details (`name`, `email`, and `address`).

### 3. What happens when you access a key that does not exist?
If you access a non-existent key using standard indexing:
```python
phone = "0000000000"
contact = contacts[phone]  # ❌ Raises KeyError!
```
Python halts execution and raises a **`KeyError`**, crashing the program if not enclosed in a `try/except` block.

### 4. How does `.get()` or `in` avoid crashes?
To avoid an unhandled `KeyError`, we use:
1. **The `in` membership operator**:
   ```python
   if phone in contacts:
       # Safe to access contacts[phone]
   ```
2. **The `.get(key, default)` method**:
   ```python
   contact = contacts.get(phone)  # Returns None (or a custom default) instead of raising KeyError
   if contact is not None:
       # Contact exists
   ```
This project uses `.get()` and `in` checks across all search, update, and delete operations to ensure the application never crashes on missing keys.

---

## 🚀 How to Run the Project

### Prerequisites
- Python 3.7 or higher (No third-party packages or `pip install` required).

### Steps
1. Open your terminal or command prompt (PowerShell / Command Prompt / bash).
2. Navigate to the project directory:
   ```powershell
   cd "C:\Users\HEMA\.gemini\antigravity\scratch\contact_book"
   ```
3. Run the script:
   ```bash
   python contact_book.py
   ```

---

## 🖥️ Sample Run & Output

```text
Welcome to Python CLI Contact Book!
Loaded 4 sample contacts.

===================================
       CONTACT BOOK MENU
===================================
 1. Add contact
 2. Search contact
 3. Update contact
 4. Delete contact
 5. View all contacts
 6. Exit
===================================
Enter your choice (1-6): 5

--- ALL CONTACTS ---
Total Contacts: 4
=====================================================================================
Phone Number    | Name                   | Email                     | Address
=====================================================================================
9876543210      | Alice Johnson          | alice@example.com         | 123 Maple Street, Springfield
9123456780      | Bob Smith              | bob@example.com           | 456 Oak Avenue, Metropolis
9988776655      | Charlie Brown          | charlie@example.com       | 789 Pine Road, Gotham
9845123456      | Diana Prince           | diana@example.com         | 321 Cedar Lane, Star City
=====================================================================================

===================================
       CONTACT BOOK MENU
===================================
 1. Add contact
 2. Search contact
 3. Update contact
 4. Delete contact
 5. View all contacts
 6. Exit
===================================
Enter your choice (1-6): 1

--- ADD NEW CONTACT ---
Enter 10-digit phone number: 9988112233
Enter contact name: David Miller
Enter email address: david@example.com
Enter physical address: 77 Sunset Strip
 Success: Contact 'David Miller' added successfully!

===================================
       CONTACT BOOK MENU
===================================
 1. Add contact
 2. Search contact
 3. Update contact
 4. Delete contact
 5. View all contacts
 6. Exit
===================================
Enter your choice (1-6): 2

--- SEARCH CONTACT ---
1. Search by Phone Number
2. Search by Name
Enter your search option (1 or 2): 2
Enter name (or part of name) to search: david

 Found 1 matching contact(s):
============================================================
Phone Number : 9988112233
Name         : David Miller
Email        : david@example.com
Address      : 77 Sunset Strip
------------------------------------------------------------
```

---

## 🧪 Testing Checklist

| Test Case | Steps to Test | Expected Behavior |
| :--- | :--- | :--- |
| **View Contacts** | Option `5` | Displays tabular listing of sample contacts |
| **Phone Validation (Letters)** | Option `1` $\rightarrow$ Enter `9876abcdef` | Rejected: Digits only required |
| **Phone Validation (Length)** | Option `1` $\rightarrow$ Enter `12345` | Rejected: Must be exactly 10 digits |
| **Duplicate Prevention** | Option `1` $\rightarrow$ Enter existing `9876543210` | Rejected: Duplicate warning displayed |
| **Name Validation** | Option `1` $\rightarrow$ Valid phone $\rightarrow$ Empty Name | Rejected: Name cannot be blank |
| **Search by Phone** | Option `2` $\rightarrow$ `1` $\rightarrow$ Enter `9876543210` | Displays Alice Johnson's details |
| **Search by Name** | Option `2` $\rightarrow$ `2` $\rightarrow$ Enter `alice` | Matches Alice Johnson (case-insensitive) |
| **Update Contact** | Option `3` $\rightarrow$ Enter phone $\rightarrow$ Press Enter to keep or type new | Values safely updated |
| **Delete (Cancel)** | Option `4` $\rightarrow$ Enter phone $\rightarrow$ Press `n` | Deletion safely cancelled |
| **Delete (Confirm)** | Option `4` $\rightarrow$ Enter phone $\rightarrow$ Press `y` | Contact removed from dictionary |
| **Missing Key Check** | Search, Update, or Delete with `0000000000` | Friendly "Not found" error, no `KeyError` |
| **Invalid Menu Option** | Enter `99` or `abc` | Friendly "Invalid choice" error |
| **Exit** | Option `6` | Exits the loop cleanly |

---

## 📂 Project Structure

```text
contact_book/
├── contact_book.py      # Core Python application code
├── README.md            # Documentation, interview explanation, and test guide
└── .gitignore           # Git ignore file for Python
```
