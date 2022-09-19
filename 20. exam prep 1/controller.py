class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def __find_player(self, player_name):
        for x in self.players:
            if x.name == player_name:
                return x

    def add_player(self, *args):
        added = []
        for player in args:
            if player not in self.players:
                added.append(player.name)
                self.players.append(player)
        return f"Successfully added: {', '.join(added)}"

    def add_supply(self, *args):
        self.supplies.extend(args)

    def sustain(self, player_name, sustenance_type):
        player = self.__find_player(player_name)
        if player is None:
            return

        if sustenance_type != 'Food' and sustenance_type != 'Drink':
            return
        idx, supply = self.__get_supply(sustenance_type)
        if supply is None:
            raise Exception(f'There are no {sustenance_type.lower()} supplies left!')

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        player.stamina += supply.energy
        if player.stamina > 100:
            player.stamina = 100
        self.supplies.pop(idx)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = self.__find_player(first_player_name)
        player2 = self.__find_player(second_player_name)

        result = ''
        if player1.stamina == 0:
            result += f'Player {player1.name} does not have enough stamina.'+'\n'
        if player2.stamina == 0:
            result += f'Player {player2.name} does not have enough stamina.'
        if result:
            return result.strip()

        if player1.stamina > player2.stamina:
            attacker, defender = player2, player1
        else:
            attacker, defender = player1, player2

        defender.stamina -= attacker.stamina / 2

        winner_check = self.__check_stamina(player1, player2)
        if winner_check:
            return f"Winner: {winner_check}"

        attacker.stamina -= defender.stamina / 2
        winner_check = self.__check_stamina(player1, player2)
        if winner_check:
            return f"Winner: {winner_check}"

        winner = player1
        if not winner_check:
            if player1.stamina < player2.stamina:
                winner = player2
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2,0)
            self.sustain(player, 'Food')
            self.sustain(player, 'Drink')

    def __str__(self):
        return '\n'. join([str(x) for x in self.players]) + "\n" + \
               '\n'. join([x.details() for x in self.supplies])


    def __get_supply(self, supply):
        for idx in range(len(self.supplies) - 1, -1, -1):
            x = self.supplies[idx]
            if x.__class__.__name__ == supply:
                return idx, x
        return (-1, None)

    def __check_stamina(self, player1, player2):
        if player1.stamina < 0:
            player1.stamina = 0
            return player2.name
        if player2.stamina < 0:
            player2.stamina = 0
            return player1.name

