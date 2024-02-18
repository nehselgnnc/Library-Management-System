class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")


    def __del__(self):
        self.file.close()


    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        for book in books:
            book_info = book.strip().split(',')
            print("Book Title:", book_info[0])
            print("Author:", book_info[1])
            print("Release Date:", book_info[2])
            print("Number of Pages:", book_info[3])
            print()


    def add_book(self):
        # Prompt user for book information
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        release_date = input("Enter the release date: ")
        num_pages = input("Enter the number of pages: ")

        # Create a string with the book information
        book_info = f"{title},{author},{release_date},{num_pages}\n"

        self.file.write(book_info)
        print("Book added successfully.")


    def remove_book(self):
        title = input("Enter the title of the book you want to remove: ")
        books = self.file.readlines()
        self.file.seek(0)

        # Create a new list excluding the book with the specified title
        new_books = [book for book in books if title not in book]

        # Truncate the file (clear its contents)
        self.file.truncate(0)

        # Write the updated list of books to the file
        self.file.writelines(new_books)
        print("Book removed successfully.")



lib = Library()


# Display the menu and execute the corresponding functionality based on user input
while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please choose again.")
