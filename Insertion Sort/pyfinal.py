from time import perf_counter
from random import shuffle
from os import system

def insertion_sort(to_sort: list, size: int) -> None:  
    for i in range(size):
        j = i

        while j > 0 and to_sort[j - 1] > to_sort[j]:  # while there is still stuff and the stuff immediatelly to the left is bigger...
            to_sort[j - 1], to_sort[j] = to_sort[j], to_sort[j - 1]  # Swap the item at current index with the item to the left.
            j -= 1

def get_perf(size: int, amount: int, verbose: bool = True) -> None:
    py_list = list(range(size))
    total_time = 0

    for i in range(amount):
        shuffle(py_list)

        start_time = perf_counter()
        insertion_sort(py_list, size)
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
