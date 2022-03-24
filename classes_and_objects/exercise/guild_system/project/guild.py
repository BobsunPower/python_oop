# from classes_and_objects.exercise.guild_system.project.player import Player
from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name, self.players = name, []

    def assign_player(self, player):
        if player.guild != "Unaffiliated" and player not in self.players:
            return f"Player {player.name} is in another guild."
        if player not in self.players:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        else:
            return f"Player {player.name} is already in the guild."

    def kick_player(self, player_name: str):
        for p in self.players:
            if p.name == player_name:
                self.players.remove(p)
                p.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        return f"Guild: {self.name}\n{''.join([p.player_info() for p in self.players])}"
