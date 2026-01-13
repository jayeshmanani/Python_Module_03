"""
Docstring for ex3.ft_achievement_tracker
This Module contains the usage of sets
"""


class Player:
    """
    Player class to store the player name along with their achievements
    """

    def __init__(self) -> None:
        """
        Init func for starting the players dictionary
        """
        self.players = dict()

    def add_player(self, name: str) -> None:
        """
        Docstring for add_player

        :param name: Name of the player
        Returns Nothing

        Initiate name stored in dict, and one can start
        storing the achievements
        """
        self.players[name] = set()

    def add_achievement(self, name: str, ac: str) -> None:
        """
        Docstring for add_achievement
        Adding the achievement for the player
        :param name: Name of the player
        :type name: str
        :param ac: Achievement needs to be added
        :type ac: str
        """
        self.players[name].add(ac)


def ft_achievement_tracker() -> None:
    """
    Demonstrating the How and What can be done using the Set and Set ops
    """
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
    inter_ac = set()
    diff_ac = set()
    for enum, p in enumerate(pl.players):
        union_ac = union_ac.union(pl.players[p])
        if enum == 0:
            inter_ac = pl.players[p]
        else:
            inter_ac = inter_ac.intersection(pl.players[p])

    player_vals = pl.players.values()
    all_achs = set()
    for s in list(player_vals):
        all_achs = all_achs.union(s)

    for i, p in enumerate(player_vals):
        others_union = set()
        for j, s in enumerate(player_vals):
            if i == j:
                continue
            others_union = others_union.union(s)

        only_p = p.difference(others_union)
        diff_ac = diff_ac.union(only_p)

    print(f"All unique achievements: {union_ac}")
    print(f"Total unique achievements: {len(union_ac)}\n")

    print(f"Common to all players: {inter_ac}")
    print(f"Rare achievements (1 player): {diff_ac}\n")

    print(f"Alice vs Bob common: "
          f"{pl.players['alice'].intersection(pl.players['bob'])}")
    print(f"Alice unique: {pl.players['alice'].difference(pl.players['bob'])}")
    print(f"Bob unique: {pl.players['bob'].difference(pl.players['alice'])}")


ft_achievement_tracker()
