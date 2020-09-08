from ability import Ability
from armor import Armor
from weapon import Weapon
import math
import random

class Hero:
    def __init__(self, name, starting_health=100, starting_mana=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.starting_mana = starting_mana
        self.current_mana = starting_mana
        self.abilities = {}
        self.weapons = {}
        self.armors = {}
        self.deaths = 0
        self.kills = 0
        self.xp = 0
        self.level = 1
    
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
        self.abilities[ability.name] = ability
    
    def add_armor(self, armor):
        self.armors[armor.name] = armor
    
    def add_weapon(self, weapon):
        self.weapons[weapon.name] = weapon

    def can_use_ability(self):
        can_attack = False
        possible_abilities = {}
        for name, ability in self.abilities:
            if ability.mana <= self.current_mana:
                possible_abilities[name] = ability
                can_attack = True
        return can_attack, possible_abilities
    
    def random_ability(self):
        ability = random.choice(self.abilities.values)
        return ability
        
    def ability_attack(self):
        can_attack, possible_abilities = self.can_use_ability()
        total_damage = 0
        while can_attack:
            ability = random.choice(possible_abilities.values)
            self.current_mana -= ability.mana
            total_damage += ability.damage
            can_attack, possible_abilities = self.can_use_ability()
        return total_damage
            
    def attack(self):
        total_damage = 0
        # for name, weapon in self.weapons:
        #     total_damage += weapon.damage
        weapon = random.choice(self.weapons.values)
        total_damage += weapon.damage
        total_damage += self.ability_attack()
        return total_damage

    def defend(self, damage_amt):
        get_defense = lambda a: a.defense
        total_defense = map(get_defense, self.armors.values)
        if total_defense > damage_amt / 2:
            total_defense = damage_amt / 2
        return total_defense
    
    def take_damage(self, damage):
        self.current_health -= damage - self.defend(damage)
    
    def is_alive(self):
        return self.current_health > 0

    def add_kill(self, num_kills=1):
        self.kills += num_kills

    def add_death(self, num_deaths=1):
        self.deaths += num_deaths

    def gain_xp(self, xp_gain=0):
        self.xp += xp_gain
        current = self.level
        self.level = math.floor((math.sqrt(2 * self.xp + 25) + 5) / 10) # Linearly rising level gap
        if self.level > current:
            self.level_up(self.level - current)

    def level_up(self, levels=1):
        for i in range(levels):
            health_gain = (self.level + 4 - i) * 2
            mana_gain = (self.level + 2 - i) * 5
            self.starting_health += health_gain
            self.starting_mana += mana_gain
        self.current_health = self.starting_health
        self.current_mana = self.starting_mana
    
    def gain_level(self, levels=1):
        necessary_xp = 0
        for i in range(levels):
            necessary_xp += (self.level + i) * 100
        self.gain_xp(necessary_xp)
    
    def print_stats(self):
        print(f"Hero Name: {self.name}\nLevel: {self.level}\nXP: {self.xp}\nHealth Pool: {self.starting_health}\nMana Pool: {self.starting_mana}\n")

hero = Hero("Hero")
hero.print_stats()
hero.gain_level(1)
hero.print_stats()
hero.gain_level(1)
hero.print_stats()
hero.gain_level(1)
hero.print_stats()
hero.gain_level(1)
hero.print_stats()
