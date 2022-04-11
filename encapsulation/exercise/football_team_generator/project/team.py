# from encapsulation.exercise.football_team_generator.project.player import Player
from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name, self.__rating, self.__players = name, rating, []

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for player in self.__players:
            if player.name == player_name:
                self.__players.remove(player)
                return player
        return f"Player {player_name} not found"
