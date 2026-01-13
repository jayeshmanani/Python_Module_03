"""
Docstring for ex4.ft_inventory_system
This Module contains the usage of Dictionaries
"""


def inventory_value(inventory: dict) -> int:
    """
    Calculate the Inventory Value

    :param inventory: Which inventory to use for calculations
    :type inventory: dict
    :return: Total amoint of inventory value
    :rtype: int
    """
    total = 0
    for item in inventory.values():
        total += item.get("quantity") * item.get("value")
    return total


def item_count(inventory: dict) -> int:
    """
    Count the no. of Items available in Inventory

    :param inventory: Which inventory to use
    :type inventory: dict
    :return: Total count value of the inventory
    :rtype: int
    """
    count = 0
    for item in inventory.values():
        count += item.get("quantity")
    return count


def category_stats(inventory: dict) -> dict:
    """
    Calculates the category wise stats of the inventory

    :param inventory: Which inventory to evaluate
    :type inventory: dict
    :return: Stats - Category wise calculation
    :rtype: dict
    """
    categories = {}
    for item in inventory.values():
        cat = item.get("category")
        qty = item.get("quantity")
        categories[cat] = categories.get(cat, 0) + qty
    return categories


def print_inventory(player: str, inventory: dict) -> None:
    """
    Print the INventory details

    :param player: For player name
    :type player: str
    :param inventory: Which inventory to use extract this info
    :type inventory: dict
    """
    print(f"=== {player}'s Inventory ===")
    for name, item in inventory.items():
        total = item.get("quantity") * item.get("value")
        print(
            f"{name} ({item.get('category')}, {item.get('rarity')}): "
            f"{item.get('quantity')}x @ {item.get('value')} gold each = {total} gold"
        )

    total_value = inventory_value(inventory)
    total_items = item_count(inventory)
    categories = category_stats(inventory)

    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {total_items} items")

    cat_str = ""
    for cat, qty in categories.items():
        cat_str += f"{cat}({qty}), "
    print("Categories:", cat_str[:-2], "\n")


def transfer_item(
        from_inv: dict,
        to_inv: dict,
        item_name: str,
        amount: int) -> bool:
    """
    Transfer the Item from A player to Another Player

    :param from_inv: Inventory of Player A (Source Account)
    :type from_inv: dict
    :param to_inv: Inventory of Player B (Destination Account)
    :type to_inv: dict
    :param item_name: Which item to trasfer
    :type item_name: str
    :param amount: How much item quantity to transfer
    :type amount: int

    Return True or False based on need for mark success or failure of the event
    """
    item = from_inv.get(item_name)
    if not item or item.get("quantity") < amount:
        print("Transaction failed!")
        return False

    item["quantity"] -= amount

    if item_name not in to_inv:
        to_inv[item_name] = dict(item)
        to_inv[item_name]["quantity"] = amount
    else:
        to_inv[item_name]["quantity"] += amount

    return True


def ft_inventory_system() -> None:
    """
    Demontration of the inventory system using dictionary in Python
    """
    print("=== Player Inventory System ===\n")

    players = {
        "Alice": {
            "sword": {
                "category": "weapon",
                "rarity": "rare",
                "quantity": 1,
                "value": 500
            },
            "potion": {
                "category": "consumable",
                "rarity": "common",
                "quantity": 5,
                "value": 50
            },
            "shield": {
                "category": "armor",
                "rarity": "uncommon",
                "quantity": 1,
                "value": 200
            }
        },
        "Bob": {
            "magic_ring": {
                "category": "armor",
                "rarity": "rare",
                "quantity": 1,
                "value": 500
            }
        }
    }

    print_inventory("Alice", players["Alice"])

    print("=== Transaction: Alice gives Bob 2 potions ===")
    if transfer_item(players["Alice"], players["Bob"], "potion", 2):
        print("Transaction successful!\n")

    print("=== Updated Inventories ===")
    print("Alice potions:", players["Alice"]["potion"]["quantity"])
    print("Bob potions:", players["Bob"]["potion"]["quantity"], "\n")

    print("=== Inventory Analytics ===")

    richest = None
    richest_value = 0
    most_items = None
    most_item_count = 0
    rare_items = {}
    for player, inv in players.items():
        value = inventory_value(inv)
        count = item_count(inv)

        if value > richest_value:
            richest_value = value
            richest = player

        if count > most_item_count:
            most_item_count = count
            most_items = player

        for name, item in inv.items():
            if item.get("rarity") == "rare":
                rare_items[name] = True

    print(f"Most valuable player: {richest} ({richest_value} gold)")
    print(f"Most items: {most_items} ({most_item_count} items)")

    rare_str = ""
    for item in rare_items.keys():
        rare_str += item + ", "
    print("Rarest items:", rare_str[:-2])


ft_inventory_system()
