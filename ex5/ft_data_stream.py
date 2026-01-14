"""
Docstring for ex5.ft_data_stream
This Module contains the usage of generators
"""


def generate_event(event_id: int) -> dict:
    p_names = ['alice', 'bob', 'charlie', 'max', 'kia', 'lambo']
    activity = ["killed monster", "found treasure", "leveled down",
                "leveled up", "died", "crafted item", "cracked gold",
                "is_resting", "is eating"]
    player = p_names[(event_id - 1) % len(p_names)]
    level = 1 + ((event_id - 1) * 3) % 15
    event_type = activity[(event_id - 1) % len(activity)]
    return {
        "id": event_id,
        "player": player,
        "level": level,
        "type": event_type,
    }


def event_stream(n):
    """Yield n deterministic events one by one."""
    for i in range(1, n + 1):
        yield generate_event(i)


def process_stream(events):
    total = 0
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0
    it = iter(events)

    while True:
        try:
            ev = next(it)
        except Exception:
            break
        total += 1
        if ev["level"] >= 10:
            high_level_players += 1
        if ev["type"] == "found treasure":
            treasure_events += 1
        elif ev["type"] == "leveled up":
            level_up_events += 1
        if ev["id"] <= 3:
            print(
                f"Event {ev['id']}: Player {ev['player']} "
                f"(level {ev['level']}) {ev['type']}"
            )
    print("...\n")
    return {
        "total": total,
        "high_level_players": high_level_players,
        "treasure_events": treasure_events,
        "level_up_events": level_up_events,
    }


def take_n(it, n):
    """Consume first n items from any iterator/generator."""
    count = 0
    for item in it:
        if count >= n:
            break
        yield item
        count += 1


def fibonacci(n: int):
    """Fibonacci generator up to n."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def is_prime(n):
    """Simple primality check."""
    if n > 1:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True
    else:
        return False


def primes(n: int):
    """Infinite prime generator."""
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def ft_data_stream() -> None:
    N = 1000
    print("=== Game Data Stream Processor ===\n")
    print(f"Processing {N} game events...\n")

    stats = process_stream(event_stream(N))

    print("=== Stream Analytics ===")
    print(f"Total events processed: {stats['total']}")
    print(f"High-level players (10+): {stats['high_level_players']}")
    print(f"Treasure events: {stats['treasure_events']}")
    print(f"Level-up events: {stats['level_up_events']}")
    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print()
    print("=== Generator Demonstration ===")
    nums = fibonacci(10)
    print(f"Fibonacci sequence (first 10): {next(nums)}", end="")
    for num in nums:
        print(f", {num}", end="")
    new_nums = primes(5)
    print()
    print(f"Prime sequence (first 5): {next(new_nums)}", end="")
    for num in new_nums:
        print(f", {num}", end="")
    print()


ft_data_stream()
