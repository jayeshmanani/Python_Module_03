"""
Docstring for ex6.ft_analytics_dashboard
This Module contains the analytics dashboard for the game events
using list comprehensions, dict comprehensions, and set comprehensions
"""


def find_category(score):
    """
    Return the Category High, Low, Medium based on score
    """
    if score >= 2100:
        return "high"
    elif score >= 1900:
        return "medium"
    return "low"


def ft_analytics_dashboard() -> None:
    players = [
        {
            "name": "alice",
            "score": 2300,
            "active": True,
            "achievements":
                [
                    "first_kill", "boss_slayer", "level_10",
                    "secret_room", "master_explorer"
                ],
            "region": "north"
        },
        {
            "name": "bob",
            "score": 1800,
            "active": True,
            "achievements":
                [
                    "first_kill", "level_5", "side_quest"
                ],
            "region": "east"
        },
        {
            "name": "charlie",
            "score": 2150,
            "active": True,
            "achievements":
                [
                    "level_10", "boss_slayer", "secret_room", "boss_slayer"
                ],
            "region": "central"
        },
        {
            "name": "diana",
            "score": 2050,
            "active": False,
            "achievements":
                [
                    "first_kill", "level_3"
                ],
            "region": "north"
        },
    ]

    print("=== Game Analytics Dashboard ===")
    print()
    print("=== List Comprehension Examples ===")

    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    scores_doubled = [p["score"] * 2 for p in players]
    active_players = [p["name"] for p in players if p["active"]]

    print("High scorers (>2000):", high_scorers)
    print("Scores doubled:", scores_doubled)
    print("Active players:", active_players)
    print()

    print("=== Dict Comprehension Examples ===")

    player_scores = {p["name"]: p["score"] for p in players if p["active"]}
    score_categories = {
        cat: len([p for p in players if find_category(p["score"]) == cat])
        for cat in ["high", "medium", "low"]
    }
    achievement_counts = {
        p["name"]: len(p["achievements"]) for p in players if p["active"]
    }

    print("Player scores:", player_scores)
    print("Score categories:", score_categories)
    print("Achievement counts:", achievement_counts)
    print()

    print("=== Set Comprehension Examples ===")

    unique_players = {p["name"] for p in players}
    unique_achievements = {
        ach for p in players for ach in p["achievements"]
    }
    active_regions = {
        p["region"] for p in players if p["active"]
    }

    print("Unique players:", unique_players)
    print("Unique achievements:", unique_achievements)
    print("Active regions:", active_regions)

    print("=== Combined Analysis ===")

    total_players = len(players)
    total_unique_achievements = len(unique_achievements)
    avg_score = sum(p["score"] for p in players) / len(players)
    top_player = max(players, key=lambda p: p["score"])

    print("Total players:", total_players)
    print("Total unique achievements:", total_unique_achievements)
    print("Average score:", avg_score)
    print(
        f"Top performer: {top_player['name']} "
        f"({top_player['score']} points, "
        f"{len(top_player['achievements'])} achievements)"
    )


if __name__ == "__main__":
    ft_analytics_dashboard()
