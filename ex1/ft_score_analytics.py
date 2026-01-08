#!/usr/bin/env python3

"""
Docstring for ex1.ft_score_analytics
This Module contains the function to analyze player scores
"""

import sys


def ft_score_analytics() -> None:
    """
    Docstring for ft_score_analytics
    :param: None
    :return: None
    This function analyzes player scores provided as command line arguments
    and computes total, average, high, low scores and score range.
    """
    print("=== Player Score Analytics ===")
    total_args = len(sys.argv)
    if total_args < 2:
        print(f"No scores provided. Usage: python3 {sys.argv[0]}"
              f" <score1> <score2> ...")
    i = 1
    scores = []
    while i < total_args:
        try:
            val = int(sys.argv[i])
            scores.append(val)
        except Exception:
            pass
        i += 1
    total_players = len(scores)
    if total_players:
        total_scores = sum(scores)
        max_score = max(scores)
        min_score = min(scores)
        print(f"Score Processed: {scores}")
        print(f"Total players: {total_players}")
        print(f"Total score: {total_scores}")
        print(f"Average score: {total_scores/total_players}")
        print(f"High score: {max_score}")
        print(f"Low score: {min_score}")
        print(f"Score range: {max_score - min_score}")


if __name__ == "__main__":
    ft_score_analytics()
