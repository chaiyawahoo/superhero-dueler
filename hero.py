from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.deaths = 0
        self.kills = 0
    
    def fight(self, opponent):
        attacker = self
        defender = opponent
        if self.abilities == 0 and opponent.abilities == 0:
            return "Draw!"
        while self.is_alive() and opponent.is_alive():
            defender.take_damage(attacker.attack())
            attacker, defender = defender, attacker
        defender.add_kill()
        attacker.add_death()
        print(f"{defender.name} won agains {attacker.name}!")
        return defender, attacker
    
    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def add_armor(self, armor):
        self.armors.append(armor)
    
    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    def defend(self, damage_amt=None):
        if damage_amt == None:
            damage_amt = 0
            for armor in self.armors:
                damage_amt += armor.max_block
            print(damage_amt)
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        if total_block > damage_amt:
            total_block = damage_amt
        return total_block
    
    def take_damage(self, damage):
        self.current_health -= damage - self.defend(damage)
    
    def is_alive(self):
        return self.current_health > 0

    def add_kill(self, num_kills=1):
        self.kills += num_kills

    def add_death(self, num_deaths=1):
        self.deaths += num_deaths