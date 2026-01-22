from heapq import heappush, heappop
from typing import List


def merge_k_lists(lists: List[List[int]]) -> List[int]:
    heap = []
    result = []

    for i, lst in enumerate(lists):
        if lst:
            heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_i, elem_i = heappop(heap)
        result.append(val)

        next_i = elem_i + 1
        if next_i < len(lists[list_i]):
            heappush(heap, (lists[list_i][next_i], list_i, next_i))

    return result


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
