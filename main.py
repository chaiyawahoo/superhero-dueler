from ability import Ability
from arena import Arena
from armor import Armor
from hero import Hero
from weapon import Weapon

if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()

