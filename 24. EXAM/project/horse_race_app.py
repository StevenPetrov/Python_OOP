from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if not self.check_horse_breed(horse_type):
            return
        if self.check_horse_name_exist(horse_name):
            pass
        if horse_type == "Appaloosa":
            horse = Appaloosa(horse_name, horse_speed)
            self.horses.append(horse)
        if horse_type == 'Thoroughbred':
            horse = Thoroughbred(horse_name, horse_speed)
            self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."


    def add_jockey(self, jockey_name: str, age: int):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")
        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.check_jockey_exist(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        horse = self.get_horse_breed(horse_type)
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse != None:
            return f"Jockey {jockey_name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."


    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.get_race_by_type(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")
        jockey = self.check_jockey_exist(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey.horse == None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."


    def start_horse_race(self, race_type: str):
        race = self.get_race_by_type(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        winner_jockey = None
        winner_horse = None
        top_speed = 0
        for jockey in race.jockeys:
            horse = jockey.horse
            if horse.speed > top_speed:
                winner_jockey = jockey
                winner_horse = horse
                top_speed = horse.speed
        return f"The winner of the {race_type} race, with a speed of {top_speed}km/h is {winner_jockey.name}! " \
               f"Winner's horse: {winner_horse.name}."








    def check_horse_name_exist(self, name):
        for horse in self.horses:
            if horse.name == name:
                raise Exception(f"Horse {name} has been already added!")
        return True

    def check_horse_breed(self, type):
        if type in ["Appaloosa", "Thoroughbred"]:
            return True
        return False

    def check_jockey_exist(self, jockey_name: str):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        return False

    def get_horse_breed(self, type):
        for horse in reversed(self.horses):
            if horse.__class__.__name__ == type and horse.is_taken == False:
                return horse
        return False

    def get_race_by_type(self, type):
        for race in self.horse_races:
            if race.race_type == type:
                return race
        return False
