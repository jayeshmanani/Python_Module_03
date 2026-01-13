"""
Docstring for ex0.ft_command_quest
This module contains the function to the command line arguments
"""

import sys


def ft_command_quest() -> None:
    """
    Docstring for ft_command_quest
    :param: None
    :return: None
    This function demonstrate how to read the System Args
    using sys.argv and what user can manipulate it
    """
    print("=== Command Quest ===")
    total_args = len(sys.argv)
    if total_args == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if total_args > 1:
        print(f"Arguments received: {total_args-1}")
        i = 1
        while (i < total_args):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1

    print(f"Total arguments: {total_args}")


ft_command_quest()
