class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name, self.__sprint, self.__dribble = name, sprint, dribble
        self.__passing, self.__shooting = passing, shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"""Player: {self.__name}
Sprint: {self.__sprint}
Dribble: {self.__dribble}
Passing: {self.__passing}
Shooting: {self.__shooting}"""
