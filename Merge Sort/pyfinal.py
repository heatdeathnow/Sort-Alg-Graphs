from time import perf_counter
from random import shuffle
from os import system

def merge_sort(to_sort: list[int], size: int) -> None:
    aux = [None] * len(to_sort)
    split_and_merge(to_sort, aux, 0, size)

def split_and_merge(to_sort: list[int], aux: list, start: int, end: int) -> tuple[int, int]:

    if end - start == 1:
        return start, end

    mid = (start + end) // 2
    
    start, mid = split_and_merge(to_sort, aux, start, mid)
    mid, end = split_and_merge(to_sort, aux, mid, end)
    
    merge_lists(to_sort, aux, start, mid, end)

    return start, end

def merge_lists(to_sort: list[int], aux: list, start: int, mid: int, end: int) -> None:
    i, j, k = start, mid, start
    
    while i < mid and j < end:
        if to_sort[i] < to_sort[j]:
            aux[k] = to_sort[i]
            i += 1
            k += 1
        
        else:
            aux[k] = to_sort[j]
            j += 1
            k += 1
    
    while i < mid:
        aux[k] = to_sort[i]
        i += 1
        k += 1

    while j < end:
        aux[k] = to_sort[j]
        j += 1
        k += 1
    
    for l in range(start, end):
        to_sort[l] = aux[l]

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
