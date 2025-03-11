import json
import os

# ------------------------- Load Library from File -------------------------

library = []

def load_library():
    global library
    if os.path.exists("library.txt"):
        try:
            with open("library.txt", "r") as file:
                library = json.load(file)
            print("📁 Library loaded successfully from file.\n")
        except:
            print("⚠ Error reading library file. Starting with an empty library.\n")
    else:
        print("📁 No existing library found. Starting fresh.\n")

# ------------------------- Save Library to File -------------------------

def save_library():
    with open("library.txt", "w") as file:
        json.dump(library, file)
    print("💾 Library saved to file. Goodbye! 👋")

# ------------------------- Add Book -------------------------

def add_book():
    print("\n📘 Add a New Book")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()

    read = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(book)
    print("✅ Book added successfully!\n")

# ------------------------- Remove Book -------------------------

def remove_book():
    print("\n📕 Remove a Book")
    title_to_remove = input("Enter the title of the book to remove: ").strip()
    found = False

    for book in library:
        if book['title'].lower() == title_to_remove.lower():
            library.remove(book)
            print("✅ Book removed successfully!\n")
            found = True
            break

    if not found:
        print("❌ Book not found in the library.\n")

# ------------------------- Search Book -------------------------

def search_book():
    print("\n🔍 Search Book")
    print("1. Search by Title")
    print("2. Search by Author")
    search_choice = input("Enter your choice (1 or 2): ").strip()

    if search_choice == "1":
        search_title = input("Enter the book title to search: ").strip()
        found_books = [book for book in library if search_title.lower() in book['title'].lower()]

    elif search_choice == "2":
        search_author = input("Enter the author name to search: ").strip()
        found_books = [book for book in library if search_author.lower() in book['author'].lower()]

    else:
        print("❌ Invalid search choice!\n")
        return

    if found_books:
        print("\n📚 Matching Books:")
        for idx, book in enumerate(found_books, start=1):
            status = "Read" if book['read'] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        print()
    else:
        print("❌ No matching books found.\n")

# ------------------------- Display All Books -------------------------

def display_all_books():
    if not library:
        print("📭 Your library is empty.\n")
    else:
        print("\n📚 Your Library:")
        for idx, book in enumerate(library, start=1):
            status = "Read" if book['read'] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        print()

# ------------------------- Show Statistics -------------------------

def display_statistics():
    total_books = len(library)

    if total_books == 0:
        print("📭 No books in the library yet.\n")
        return

    read_books = sum(1 for book in library if book['read'])
    percentage_read = (read_books / total_books) * 100

    print("\n📊 Library Statistics:")
    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Percentage read: {percentage_read:.2f}%\n")

# ------------------------- Main Program -------------------------

load_library()

while True:
    print("===== 📚 Personal Library Manager =====")
    print("Select an option:")
    print("1. Add a book ➕")
    print("2. Remove a book 🗑️")
    print("3. Search for a book 🔍")
    print("4. Display all books 📖")
    print("5. Display statistics 📊")
    print("6. Exit & Save 💾")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        display_all_books()
    elif choice == "5":
        display_statistics()
    elif choice == "6":
        save_library()
        break
    else:
        print("❌ Invalid choice! Please try again.\n")
