from ability import Ability
from arena import Arena
from armor import Armor
from hero import Hero
from weapon import Weapon

if __name__ == "__main__":
    game_is_running = True
    arena = Arena()

    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        if play_again.lower() == "n":
            game_is_running = False

        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()