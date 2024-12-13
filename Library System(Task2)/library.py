from book import Book
import re
import os


class Library:
    registered_books = []
    biggest_name = 5
    biggest_author = 6

    @staticmethod
    def valid_year(publication_year):
        if publication_year.isdigit() and int(publication_year) > 0:
            return True
        else:
            return False

    @staticmethod
    def add():
        name = str(input("Enter The Book's Title: "))
        Library.biggest_name = max(len(name), Library.biggest_name)
        author = str(input("Enter The Book's Author: "))
        Library.biggest_author = max(len(author), Library.biggest_author)

        publication_year = input("Enter year of Publication: ")
        while not Library.valid_year(publication_year):
            publication_year = input(f"Please enter a valid Year for the book \"{name}\": ")
        Library.registered_books.append(Book(name, author, int(publication_year), False))
        print(f"Book \"{name}\" has been added to the Library!")

    @staticmethod
    def find_book():
        name = input("Enter The Title of the book: ")
        found_unavailable = False
        for index in range(len(Library.registered_books)):
            if Library.registered_books[index].title == name:
                if not Library.registered_books[index].is_borrowed:
                    return True, "Book is Found!", index
                else:
                    found_unavailable = True
                    index_unavailable = index
        if found_unavailable:
            return False, "Found the Book, However it's not available for Borrowing :(", index_unavailable
        else:
            return False, f"Haven't found a Book with the title \"{name}\"."

    @staticmethod
    def borrow_book():
        found = Library.find_book()
        if found[0]:
            Library.registered_books[found[2]].borrow()
            print("Book Borrowed!")
        else:
            print(found[1])

    @staticmethod
    def return_book():
        found = Library.find_book()
        if not found[0]:
            if len(found) == 3:
                Library.registered_books[found[2]].Return()
                print("Book Returned!")
            else:
                print(found[1])
        else:
            print(f"The Book is already in our Bookshelf and ready for borrowing again! :)")

    @staticmethod
    def open_file(open_type):
        filename = input("Enter File Name: ")
        while filename[-4:] != ".txt" or not (os.path.exists(filename)) and open_type != "w":
            print(
                f"The File Name you entered \"{filename}\" doesn't exist. Try Again"
                f"\nMake Sure You're typing the format of the text \".txt\"")
            filename = input("Enter File Name: ")

        file = open(filename, open_type)
        return file

    @staticmethod
    def view_books(borrow_only=False, show_both=False):
        print("\n\n")
        name_length = Library.biggest_name + 2
        author_length = Library.biggest_author + 2
        horizon_length = name_length + author_length + 18 + 11 + 10
        header = "**Book Menu**".center(horizon_length)
        print(header)
        print("=" * horizon_length)
        print("||" + (" " * name_length) + "||" + (" " * author_length) + "||" + (" " * 18) + "||" + (" " * 11) + "||")
        print("||" + "Title".center(name_length) + "||" + "Author".center(author_length)
              + "||" + "Publication Year".center(18) + "||" + "State".center(11) + "||")
        print("||" + (" " * name_length) + "||" + (" " * author_length) + "||" + (" " * 18) + "||" + (" " * 11) + "||")
        print("=" * horizon_length)
        for book in Library.registered_books:
            if book.is_borrowed and (borrow_only or show_both):
                print("||" + book.title.center(name_length) + "||" + book.author.center(author_length)
                      + "||" + str(book.publication_year).center(18) + "||" + "Borrowed".center(11) + "||")
            elif not book.is_borrowed and (not borrow_only or show_both):
                print("||" + book.title.center(name_length) + "||" + book.author.center(author_length)
                      + "||" + str(book.publication_year).center(18) + "||" + "Available".center(11) + "||")
        print("=" * horizon_length)

    @staticmethod
    def load_books():
        book_pattern = r'''\s*(\w|\w[\w',\?!\s]*\w[\.\?!]?)\s*      #Book Title
        \W+\s*(\w|\w[\w',\?!\s]*\w[\.\?!]?)\s*      #Book Author
        \W+\s*(\d{4})\s*      #Year_of_Publication
        \W+\s*(borrowed|available)\s*               #State
        '''
        book_pattern = re.compile(book_pattern, re.VERBOSE | re.IGNORECASE)
        file = Library.open_file("r")
        for book in file:
            match = re.search(book_pattern, book)
            if match:
                title = match.group(1)
                Library.biggest_name = max(len(title), Library.biggest_name)
                author = match.group(2)
                Library.biggest_author = max(len(author), Library.biggest_author)
                year = int(match.group(3))
                if match.group(4).lower() == "borrowed":
                    state = True
                else:
                    state = False
                Library.registered_books.append(Book(title, author, year, state))
        file.close()
        print("Books have been Loaded into Library!")

    @staticmethod
    def save_books():
        file = Library.open_file("w")
        name_length = Library.biggest_name + 2
        author_length = Library.biggest_author + 2
        horizon_length = name_length + author_length + 18 + 11 + 10
        header = "**Book Menu**".center(horizon_length)
        file.write(header + "\n")
        file.write("=" * horizon_length + "\n")
        file.write("||" + (" " * name_length) + "||" + (" " * author_length) + "||" + (" " * 18) + "||" + (" " * 11) + "||" + "\n")

        file.write("||" + "Title".center(name_length) + "||" + "Author".center(author_length)
                    + "||" + "Publication Year".center(18) + "||" + "State".center(11) + "||" + "\n")

        file.write("||" + (" " * name_length) + "||" + (" " * author_length) + "||" + (" " * 18) + "||" + (" " * 11) + "||" + "\n")
        file.write("=" * horizon_length + "\n")
        for book in Library.registered_books:
            if book.is_borrowed:
                file.write("||" + book.title.center(name_length) + "||" + book.author.center(author_length)
                            + "||" + str(book.publication_year).center(18) + "||" + "Borrowed".center(11) + "||" + "\n")
            else:
                file.write("||" + book.title.center(name_length) + "||" + book.author.center(author_length)
                            + "||" + str(book.publication_year).center(18) + "||" + "Available".center(11) + "||" + "\n")
        file.write("=" * horizon_length + "\n")
        file.close()
        print("Book Menu Saved Successfully!")
