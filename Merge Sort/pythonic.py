from time import perf_counter
from random import shuffle
from os import system

def merge_sort(to_sort: list[int], size: int) -> None:
    sorted = split_and_sort(to_sort, size)
    to_sort = sorted

def split_and_sort(to_sort: list[int], size: int) -> list[int]:

    if size == 1:
        return to_sort

    mid = size // 2
    remainder = size % 2  # Either 0 or 1

    left = split_and_sort(to_sort[ : mid], mid)
    right = split_and_sort(to_sort[mid : ], mid + remainder)
    
    return merge_lists(left, right)

def merge_lists(left: list[int], right: list[int]) -> list[int]:
    i, j = 0, 0
    sorted: list[int] = []
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        
        else:
            sorted.append(right[j])
            j += 1
    
    if i < len(left):
        sorted.extend(left[i : ])

    elif j < len(right):
        sorted.extend(right[j : ])
    
    return sorted

def get_perf(size: int, amount: int, verbose: bool = True) -> float:
    to_sort = list(range(size))
    total_time = 0.0

    for i in range(amount):
        shuffle(to_sort)

        start_time = perf_counter()
        merge_sort(to_sort, size)
        end_time = perf_counter()

        elapsed_time = end_time - start_time

        if i == 0:
            worst_case, best_case = elapsed_time, elapsed_time
        
        elif elapsed_time > worst_case:
            worst_case = elapsed_time
        
        elif elapsed_time < best_case:
            best_case = elapsed_time
        
        total_time += elapsed_time

    mean_time = total_time / amount

    if verbose:
        system('cls')
        print((f"""Analysis of time taken to sort {amount} lists of size {size}.
    Mean time: {mean_time:.2f} seconds.
    Best case scenario: {best_case:.2f} seconds.
    Worst case scenario: {worst_case:.2f} seconds."""))

    return mean_time
