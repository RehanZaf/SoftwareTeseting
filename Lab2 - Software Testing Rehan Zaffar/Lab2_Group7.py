"""
Name: Rehan Zaffar ID: 100973932
Date: Feb 7th, 2025
Description: add, list, delete, search, books from a list.
"""

import csv

# Function to add a book to the reading list
def add_book(title, author, year):
    with open('books.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, year])
    print(f'Book "{title}" added successfully!')


# Function to list all books
def list_books():
    try:
        with open('books.csv', mode='r') as file:
            reader = csv.reader(file)
            books = list(reader)
            print("\nReading List:")
            for row in books[0:]:
                print(f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
    except FileNotFoundError:
        print("File not found")


# Function to search for a book by title
def search_book(title):
    try:
        with open('books.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() == title.lower():
                    print(f'Found: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
                    return
        print('Book not found')
    except FileNotFoundError:
        print("File not found")


# Function to delete a book
def delete_book(title):
    found = False
    try:
        with open('books.csv', mode='r') as file:
            reader = csv.reader(file)
            books = list(reader)

        with open('books.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in books[0:]:
                if row[0].lower() != title.lower():
                    writer.writerow(row)
                else:
                    found = True

        if found:
            print(f'Book "{title}" deleted successfully.')
        else:
            print("Book not found.")

    except FileNotFoundError:
        print("File not found")


# Menu loop
def menu():
    while True:
        print("\n1. Add Book\n2. List Books\n3. Search Book\n4. Delete Book\n5. Quit")
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter book title: ").strip()
            if not title:
                print("Invalid book title. Try again.")
                continue

            author = input("Enter author name: ").strip()
            if not author:
                print("Invalid author name. Try again.")
                continue

            year = input("Enter year of publication: ").strip()
            if not year.isdigit() or int(year) > 2025 or int(year) < 0:
                print("Invalid year. Enter a valid year.")
                continue

            add_book(title, author, year)

        elif choice == '2':
            list_books()

        elif choice == '3':
            title = input("Enter book title to search: ").strip()
            search_book(title)

        elif choice == '4':
            title = input("Enter book title to delete: ").strip()
            delete_book(title)

        elif choice == '5':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


# Run the program
if __name__ == "__main__":
    menu()
