from time import perf_counter
from random import shuffle
from os import system

def selection_sort(to_sort: list[int], size: int) -> None:
    for i in range(size - 1):

        min_pos = i
        for j in range(i + 1, size):
            if to_sort[j] < to_sort[min_pos]:
                min_pos = j
                
        to_sort[i], to_sort[min_pos] = to_sort[min_pos], to_sort[i]

def get_perf(size: int, amount: int, verbose: bool = True) -> None:
    py_list = list(range(size))
    total_time = 0
    
    for i in range(amount):
        shuffle(py_list)

        start_time = perf_counter()
        selection_sort(py_list, size)
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
