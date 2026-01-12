#!/usr/bin/env python3

"""
Docstring for ex3.ft_achievement_tracker
This Module contains the usage of sets
"""


class Player:
    def __init__(self):
        self.players = dict()

    def add_player(self, name):
        self.players[name] = set()

    def add_achievement(self, name, ac):
        self.players[name].add(ac)


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===")
    print()

    acs = {'alice': ['first_kill', 'level_10', 'treasure_hunter',
                     'speed_demon'],
           'bob': ['first_kill', 'level_10', 'boss_slayer', 'collector'],
           'charlie': ['level_10', 'treasure_hunter',
                       'boss_slayer', 'speed_demon', 'perfectionist']}
    pl = Player()
    players = ['alice', 'bob', 'charlie']
    for p in players:
        pl.add_player(p)
    for k, v in acs.items():
        for v1 in v:
            pl.add_achievement(k, v1)
    for p in pl.players:
        print(f"Player {p} achievements: {pl.players[p]}")

    print("\n=== Achievement Analytics ===")
    union_ac = set()
    for p in pl.players:
        union_ac = union_ac.union(pl.players[p])

    print(f"All unique achievements: {union_ac}")
    print(f"Total unique achievements: {len(union_ac)}")


if __name__ == "__main__":
    ft_achievement_tracker()
