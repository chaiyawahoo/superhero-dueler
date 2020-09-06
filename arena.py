from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None
    
    def create_ability(self):
        name = input("What is the ability name?\n")
        max_damage = int(input("What is the max damage of the ability?\n"))
        return Ability(name, max_damage)
    
    def create_weapon(self):
        name = input("What is the weapon name?\n")
        max_damage = int(input("What is the max damage of the weapon?\n"))
        return Weapon(name, max_damage)
    
    def create_armor(self):
        name = input("What is the armor name?\n")
        max_block = int(input("What is the max block of the armor?\n"))
        return Armor(name, max_block)
    
    def create_hero(self):
        hero_name = input("Hero's name:\n")
        hero_health = int(input(f"How much health does {hero_name} have?\n"))
        hero = Hero(hero_name, hero_health)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice:\n")
           if add_item == "1":
               ability = self.create_ability()
               hero.add_ability(ability)
           elif add_item == "2":
               weapon = self.create_weapon()
               hero.add_weapon(weapon)
           elif add_item == "3":
               armor = self.create_armor()
               hero.add_armor(armor)
        return hero
    
    def build_team(self):
        team_name = input("What would you like to call this team?\n")
        team = Team(team_name)
        num_members = int(input(f"How many members would you like on {team_name}?\n"))
        for i in range(num_members):
            hero = self.create_hero()
            team.add_hero(hero)
        return team
    
    def build_team_one(self):
        self.team_one = self.build_team()

    def build_team_two(self):
        self.team_two = self.build_team()

    def team_battle(self):
        self.team_one.attack(self.team_two)
    
    def get_team_stats(self, team):
        print(f"\n{team.name} statistics: ")
        team.stats()
    
    def get_team_avg_kd(self, team):
        team_kills = 0
        team_deaths = 0
        for hero in team.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(f"\n{team.name}\'s average K/D was: {team_kills/team_deaths}")
    
    def get_team_survivors(self, team):
        for hero in team.heroes:
            if hero.deaths == 0:
                print(f"Survived from {team.name}: {hero.name}")
    
    def show_stats(self):
        self.get_team_stats(self.team_one)
        self.get_team_stats(self.team_two)

        self.get_team_avg_kd(self.team_one)
        self.get_team_avg_kd(self.team_two)

        self.get_team_survivors(self.team_one)
        self.get_team_survivors(self.team_two)