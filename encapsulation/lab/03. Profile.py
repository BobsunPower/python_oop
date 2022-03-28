class Profile:
    def __init__(self, username: str, password: str):
        self.username, self.password = username, password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username: str):
        if 5 <= len(username) <= 15:
            self.__username = username
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return f'{"*" * len(self.__password)}'

    @password.setter
    def password(self, password: str):
        if len(password) >= 8 \
                and len([x for x in password if x.isnumeric()]) > 0 \
                and len([x for x in password if x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']) > 0:
            self.__password = password
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'
