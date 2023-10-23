from os import system
from random import shuffle
from time import perf_counter

def bubble_sort(to_sort: list[int], size: int) -> None:
    swapped = True

    while swapped:
        swapped = False  # Se fizer um passe sem mudar nada, está em ordem.

        for i in range(1, size):
            if to_sort[i] < to_sort[i - 1]:  # Se usar i + 1 vai dar IndexError.
                to_sort[i], to_sort[i - 1] = to_sort[i - 1], to_sort[i]
                swapped = True

def get_perf(size: int, amount: int, verbose: bool = True) -> None:
    to_sort = list(range(size))
    total_time = 0.0

    for i in range(amount):
        shuffle(to_sort)

        start_time = perf_counter()
        bubble_sort(to_sort, size)
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
