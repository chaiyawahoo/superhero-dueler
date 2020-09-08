from weapon import Weapon

class Ability:
    def __init__(self, name, damage, mana):
        super().__init__(name, damage)
        self.mana = mana