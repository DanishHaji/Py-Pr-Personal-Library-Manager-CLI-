import json # For optional file handling

# Load existing Library from a file (if available)
def load_library():
    try:
        with open('library.json', 'r') as file:
            return json.load(file) # Ensure to return the loaded library
    except FileNotFoundError:
        return [] # Return an empty list if the file is not found
    
# Save Library Data to a file
def save_library_to_file(library):
    with open("library.txt", "w") as file:
        for book in library:
            file.write(f"{book['title']}|{book['author']}|{book['year']}|{book['genre']}|{'read' if book['read'] else 'unread'}\n")

# Load Library from a text file
def load_library_from_file():
    library = []
    try:
        with open('library.txt', 'r') as file:
            for line in file:
                title, author, year, genre, read_status = line.strip().split("|")
                book = {
                    "title": title,
                    "author": author,
                    "year": year,
                    "genre": genre,
                    "read": (read_status == "read")
                }
                library.append(book)
    except FileNotFoundError:
        # If the file doesn't exist, return an empty library
        return []
    return library

# Function to add a new book
def add_book(library):
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    year = input("Enter publication year: ").strip()
    genre = input("Enter genre: ").strip()
    read = input("Have you read the book? (y/n): ").strip().lower() == "y"
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print(f"\n✅ Book '{title}' added successfully!\n")
    save_library_to_file(library)

# Function to remove a book by title
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() ==title.lower():
            library.remove(book)
            print(f"\n✅ Book '{title}' removed successfully!\n")
            save_library_to_file(library)
            return
    print("\n❌ Book not found!\n")

# Function to search for books by title or author
def search_book(library):
    search_book = input("Search for books by title or author: ").strip().lower()
    found_books = [book for book in library if search_book in book["title"].lower() or search_book in book["author"].lower()]

    if found_books:
        print("\n🔍 Search Results: ")
        for book in found_books:
            print(f"-.{book['title']} by {book['author']} ({book['year']})")
    else:
        print("\n❌ No books found matching the search term!\n")

# Function to display all books
def display_books(library):
    if not library:
        print("\n📚 There are no books in the library.\n")
        return

    print("\n📚 Your Library:")
    for idx, book in enumerate(library, 1):
        status = "✅ Read" if book["read"] else "📖 Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} [{status}]")

# Function to display library statistics
def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0

    print("\n📊 Library Statistics:")
    print(f" Total books: {total_books}")
    print(f"✅ Books read: {read_books} ({read_percentage:.2f}% read)\n")

# Main program loop
def main():
    library = load_library_from_file() # Load library data from 'library.txt' 

    while True:
        print("\n📖 Personal Library Management System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for books")
        print("4. Display all books")
        print("5. Display library statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("\n📖 Thanks for using the library management system! Goodbye!\n")
            save_library_to_file(library) # Save the library data to 'library.txt'
            break
        else:
            print("\n❌ Invalid choice! Please enter a number between 1 and 6.\n")

# Run the main program
if __name__ == "__main__":
    main()    
