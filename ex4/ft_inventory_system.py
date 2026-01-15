"""
Docstring for ex4.ft_inventory_system
This Module contains the usage of Dictionaries
"""


import sys
from typing import Dict, List, Tuple


def parse_args_to_inventory(argv: List[str]) -> Dict[str, int]:
    """
    Convert command line args like ['sword:1', 'potion:5'] to:
    {'sword': 1, 'potion': 5}
    """
    inventory = dict()

    for arg in argv:
        if ":" not in arg:
            continue

        name, qty_str = arg.split(":", 1)
        name = name.strip()

        try:
            quantity = int(qty_str)
        except ValueError:
            continue

        current_qty = inventory.get(name, 0)
        inventory.update({name: current_qty + quantity})

    return inventory


def compute_totals(inventory: Dict[str, int]) -> Tuple[int, int]:
    """
    Return (total_quantity, unique_items).
    """
    total_quantity = sum(inventory.values())
    unique_items = len(inventory.keys())
    return total_quantity, unique_items


def sort_inventory_by_quantity(
        inventory: Dict[str, int]
) -> List[Tuple[str, int]]:
    """
    Return list of (name, quantity) sorted by quantity descending.
    """
    return sorted(inventory.items(), key=lambda kv: kv[1], reverse=True)


def find_most_least_abundant(
    sorted_items: List[Tuple[str, int]]
) -> Tuple[str | None, int, str | None, int]:
    """
    Given sorted list [(name, qty), ...] (descending), return
    (most_name, most_qty, least_name, least_qty).
    most_name / least_name can be None if list is empty.
    """
    if not sorted_items:
        return None, 0, None, 0

    most_name, most_qty = sorted_items[0]
    least_name, least_qty = sorted_items[-1]
    return most_name, most_qty, least_name, least_qty


def categorize_items(
    inventory: Dict[str, int],
    total_quantity: int,
) -> Dict[str, Dict[str, int]]:
    """
    Create categories like:
      {
        "Moderate": {"potion": 5},
        "Scarce": {"sword": 1, "shield": 2, ...}
      }
    """
    categories = {
        "Moderate": dict(),
        "Scarce": dict(),
    }

    if not inventory:
        return categories

    avg = total_quantity / len(inventory)

    for name, qty in inventory.items():
        if qty >= avg:
            categories["Moderate"].update({name: qty})
        else:
            categories["Scarce"].update({name: qty})

    return categories


def management_suggestions(
    inventory: Dict[str, int],
    threshold: int = 2,
) -> List[str]:
    """
    Return list of items that should be restocked.
    """
    restock = []
    for name, qty in inventory.items():
        if qty <= threshold:
            restock.append(name)
    return restock


def print_inventory_analysis(inventory: Dict[str, int]) -> None:
    total_quantity, unique_items = compute_totals(inventory)
    sorted_items = sort_inventory_by_quantity(inventory)
    most_name, most_qty, least_name, least_qty = find_most_least_abundant(
        sorted_items)
    categories = categorize_items(
        inventory, total_quantity)
    restock = management_suggestions(inventory)

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_quantity}")
    print(f"Unique item types: {unique_items}")
    print()
    print("=== Current Inventory ===")
    for name, qty in sorted_items:
        if total_quantity > 0:
            percent = (qty / total_quantity) * 100
        else:
            percent = 0.0
        print(f"{name}: {qty} units ({percent:.1f}%)")
    print()
    print("=== Inventory Statistics ===")
    if most_name is not None:
        print(f"Most abundant: {most_name} ({most_qty} units)")
        print(f"Least abundant: {least_name} ({least_qty} units)")
    else:
        print("Inventory is empty.")
    print()
    print("=== Item Categories ===")
    for category_name, items_dict in categories.items():
        print(f"{category_name}: {items_dict}")
    print()
    print("=== Management Suggestions ===")
    print(f"Restock needed: {restock}")
    print()
    print("=== Dictionary Properties Demo ===")
    keys_list = list(inventory.keys())
    values_list = list(inventory.values())
    print(f"Dictionary keys: {keys_list}")
    print(f"Dictionary values: {values_list}")

    sample_key = "sword"
    in_inventory = sample_key in inventory.keys()
    print(f"Sample lookup - '{sample_key}' in inventory: {in_inventory}")


def ft_inventory_system() -> None:
    args = sys.argv[1:]
    inventory = parse_args_to_inventory(args)
    print_inventory_analysis(inventory)


ft_inventory_system()
