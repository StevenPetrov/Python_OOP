from project.player import Player


class Guild:
    players = []

    def __init__(self, name):
        self.name = name

    def assign_player(self, player: Player):
        if player not in self.players and player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player not in self.players and player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        return f"Player {player.name} is already in the guild."

    def kick_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player_name)
                player_name.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f'Guild: {self.name}\n'
        for player in self.players:
            result += player.player_info() + '\n'
        return result.strip()


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
