"""

"""
from utils import my_database_JSON

user_choice = """
-> 'a' to add a new book
-> 'l' to list all books
-> 'r' to mark a book as read
-> 'd' to delete a book
-> 'q' to quit

Your choice: """

def menu():
    my_database_JSON.create_book_table()
    user_input = input(user_choice)
    while user_input != "q":
        if user_input == "a":
            prompt_add_book()
        elif user_input == "l":
            list_books()
        elif user_input == "r":
            prompt_read_books()
        elif user_input == "d":
            prompt_delete_book()
        else:
            print("Unknown command. Please try again.")
        user_input = input(user_choice)


# def prompt_add_book()  ---> ask for book name and author
def prompt_add_book():
    user_book = input("Please type the name of the desired book: ")
    user_author = input("Please type the name of the author: ")

    my_database_JSON.add_book(user_book, user_author)


# def list_books() ----> show all books in our list
def list_books():
    books = my_database_JSON.get_all_books()
    for book in books:
        read = "YES" if book["read"] else "NO"
        print(f"{book["name"]} by {book["author"]}, read: {read}")


# def prompt_read_books() ---> ask for book name and change it to "read" in our list
def prompt_read_books():
    user_input =  input("Please write the name of the book you want to mark as 'read': ")

    my_database_JSON.mark_book_as_read(user_input)


# def prompt_delete_books() ---> ask for book name and remove book from list
def prompt_delete_book():
    user_input = input("Type in the name of the book you want to remove: ")

    my_database_JSON.delete_book(user_input)

menu()