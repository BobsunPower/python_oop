# TODO
# 92/100
# TO FIND BETTER SOLUTION
# from classes_and_objects.exercise.library.project.user import User
# from classes_and_objects.exercise.library.project.library import Library
from project.user import User
from project.library import Library


class Registration:
    BLOCK_REGISTRATION_OF_SAME_USERNAME_OR_ID = True
    BLOCK_NAMECHANGE_IF_USED_BY_OTHER_USER = True
    REMOVE_LIBRARY_RENTED_RECORD_ON_USER_DELETE = True

    def __init__(self) -> None:
        pass

    def add_user(self, user: User, library: Library) -> str:

        if Registration.BLOCK_REGISTRATION_OF_SAME_USERNAME_OR_ID:
            check = True
            if user.username in [u.username for u in library.user_records] \
                    or user.id in [u.id for u in library.user_records]:
                check = False
        else:
            check = True

        if user not in library.user_records and check:
            library.user_records.append(user)
        else:
            return f"User with id = {user.id} already registered in the library!"

    def remove_user(self, user: User, library: Library) -> str:
        if user in library.user_records:
            library.user_records.remove(user)

            if Registration.REMOVE_LIBRARY_RENTED_RECORD_ON_USER_DELETE:
                if user.username in library.rented_books.keys():
                    library.rented_books.pop(user.username)

        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library) -> str:
        if Registration.BLOCK_NAMECHANGE_IF_USED_BY_OTHER_USER:
            filtered_records = [u.username for u in library.user_records]
        else:
            filtered_records = [u.username for u in library.user_records if u.id == user_id]

        if user_id not in [u.id for u in library.user_records]:
            return f"There is no user with id = {user_id}!"

        if new_username in filtered_records:
            return f"Please check again the provided username - " \
                   f"it should be different than the username used so far!"

        u = [u for u in library.user_records if u.id == user_id][0]
        old_username = u.username
        u.username = new_username
        if old_username in library.rented_books.keys():
            library.rented_books[new_username] = library.rented_books.pop(old_username)
        return f'Username successfully changed to: {new_username} for userid: {user_id}'
