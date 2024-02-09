"""
This will be concerned with storing and retrieving books from a csv file.
"""
books_file = "my_books.txt"

def create_book_table():
    with open(books_file, "w"):
        pass

def add_book(name, author):
    with open(books_file, "a") as file:
        file.write(f"{name}, {author}, 0\n")


def get_all_books():
    with open(books_file, "r") as file:
        lines = [line.strip().split(",") for line in file.readlines()]
    return [
        {"name": line[0].strip(), "author": line[1].strip(), "read": line[2].strip()}
        for line in lines
    ]


def mark_book_as_read(user_input):
    books = get_all_books()
    for book in books:
        if book["name"] == user_input:
            book["read"] = "1"
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, "w") as file:
        for book in books:
            file.write(f"{book['name']}, {book['author']}, {book['read']}\n")


def delete_book(user_input):
    books = get_all_books()
    books = [book for book in books if book["name"] != user_input]
    _save_all_books(books)


# def delete_book(name):
#     for book in books:
#         if book["name"] == name:
#             books.remove(book)



# print(__name__)

