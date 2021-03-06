# TODO
# 92/100
# TO FIND BETTER SOLUTION
# from classes_and_objects.exercise.library.project.user import User
from project.user import User


class Library:
    REMOVE_AUTHOR_FROM_AVAILABLE_IF_EMPTY = True
    CHECK_SO_USER_DONT_TAKE_BOOK_TWICE = True
    FIND_MIN_RETURN_DATE = True
    REMOVE_USER_FROM_RENTED_BOOKS_IF_EMPTY = True

    def __init__(self) -> None:
        self.user_records = []
        self.books_available = {}  # {author: [book_name, ]}
        self.rented_books = {}  # {usernames: {book names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:

        if Library.CHECK_SO_USER_DONT_TAKE_BOOK_TWICE:
            check = (book_name not in user.books)
        else:
            check = True

        if book_name in self.books_available.get(author, []) and check:

            user.books.append(book_name)

            if user.username not in self.rented_books.keys():
                self.rented_books[user.username] = {}
            self.rented_books[user.username].update({book_name: days_to_return})

            self.books_available[author].remove(book_name)

            if Library.REMOVE_AUTHOR_FROM_AVAILABLE_IF_EMPTY:
                if len(self.books_available.get(author, [])) == 0:
                    self.books_available.pop(author)

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        elif book_name in [b for u in self.rented_books.keys() for b in self.rented_books[u].keys() if b == book_name]:
            return_days = []
            for u in self.rented_books.keys():
                for b in self.rented_books[u].keys():
                    if b == book_name:
                        return_days.append(self.rented_books[u][b])

            if Library.FIND_MIN_RETURN_DATE:
                return_days.sort()

            return f'The book "{book_name}" is already rented and will be ' \
                   f'available in {return_days[0]} days!'

    def return_book(self, author: str, book_name: str, user: User) -> str:
        if book_name in user.books:
            user.books.remove(book_name)

            self.rented_books[user.username].pop(book_name)

            if Library.REMOVE_USER_FROM_RENTED_BOOKS_IF_EMPTY:
                if len(self.rented_books[user.username]) == 0:
                    self.rented_books.pop(user.username)

            if author not in self.books_available.keys():
                self.books_available[author] = []
            self.books_available[author].append(book_name)

        else:
            return f"{user.username} doesn't have this book in his/her records!"
