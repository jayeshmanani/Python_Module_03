"""
Docstring for ex2.ft_coordinate_system
This Module contains the function to create and manipulate 3D coordinates
using tuples.
"""

import math
import sys


def create_position(x: int, y: int, z: int) -> tuple[int, int, int]:
    """
    Create a 3D position as an immutable tuple.
    """
    return (x, y, z)


def distance_3d(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> float:
    """
    Calculate the Euclidean distance between two 3D points.
    """
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(coord_string: str) -> tuple | None:
    """
    Parse a string of coordinates "x,y,z" into a 3D position tuple.
    """
    try:
        parts = coord_string.split(',')
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        return (x, y, z)
    except Exception as e:
        print("Error parsing coordinates:", e)
        print("Error details - Type:", type(e).__name__ + ",", "Args:", e.args)
        return None


def ft_coordinate_system() -> None:
    """
    Main function to demonstrate coordinate system functionalities.
    """
    print("=== Game Coordinate System ===\n")
    pos = create_position(10, 20, 5)
    print("Position created:", pos)

    origin = (0, 0, 0)
    dist = distance_3d(origin, pos)
    print(f"Distance between {origin} and {pos}: {dist:.2f}")
    print()
    coord_str = "3,4,0"
    print(f'Parsing coordinates: "{coord_str}"')
    parsed = parse_coordinates(coord_str)
    if parsed:
        print("Parsed position:", parsed)
        print(f"Distance between {origin} and"
              f" {parsed}: {distance_3d(origin, parsed)}")
    print()
    invalid_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_str}"')
    parse_coordinates(invalid_str)
    print()
    print("Unpacking demonstration:")
    if parsed:
        x, y, z = parsed
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    print()
    if len(sys.argv) == 2:
        input_str = sys.argv[1]
        print(f'Parsing input coordinates: "{input_str}"')
        parsed = parse_coordinates(input_str)
        print()
        print("Unpacking demonstration:")
        if parsed:
            x, y, z = parsed
            print(f"Player at x={x}, y={y}, z={z}")
            print(f"Coordinates: X={x}, Y={y}, Z={z}")


ft_coordinate_system()
