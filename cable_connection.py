from heapq import heapify, heappop, heappush
from typing import List, Tuple


def min_cable_connection_cost(lengths: List[int | float]) -> Tuple[float, List[tuple]]:
    if any((not isinstance(x, (int, float))) or x < 0 for x in lengths):
        raise ValueError("All cable lengths must be non-negative numbers")

    if len(lengths) <= 1:
        return 0, []

    heap = lengths[:]
    heapify(heap)

    total = 0
    steps = []

    while len(heap) > 1:
        a = heappop(heap)
        b = heappop(heap)
        cost = a + b
        total += cost
        steps.append((a, b, cost))
        heappush(heap, cost)

    return total, steps


if __name__ == "__main__":
    cables = [8, 4, 6, 12]
    total, steps = min_cable_connection_cost(cables)

    print("Steps:")
    for a, b, cost in steps:
        print(f"  {a} + {b} = {cost}")

    print("Total cost:", total)
