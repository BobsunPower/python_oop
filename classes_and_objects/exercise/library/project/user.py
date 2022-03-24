# TODO
# 92/100
# TO FIND BETTER SOLUTION
class User:
    RETURN_SORTED_BOOKS_IN__STR__ = False

    def __init__(self, user_id: int, username: str) -> None:
        self.id = user_id
        self.user_id = user_id
        self.username = username
        self.books = []

    def info(self) -> str:
        if self.books:
            retval = sorted(self.books)
            return ', '.join(retval)

    def __str__(self) -> str:
        return f"{self.id}, {self.username}, " \
               f"{sorted(self.books) if User.RETURN_SORTED_BOOKS_IN__STR__ else self.books}"
