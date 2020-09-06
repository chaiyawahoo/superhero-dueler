import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
    
    def add_hero(self, hero):
        self.heroes.append(hero)
    
    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0
    
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
    
    def stats(self):
        for hero in self.heroes:
            if hero.deaths == 0:
                hero.deaths = 1
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths: {kd}")
    
    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
    
    def attack(self, other_team):
        living_heroes = self.heroes[:]
        living_opponents = other_team.heroes[:]

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)
            winner, loser = hero.fight(opponent)
            if loser in living_heroes:
                living_heroes.remove(loser)
            else:
                living_opponents.remove(loser)