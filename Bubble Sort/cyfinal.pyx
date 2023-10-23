#cython: language_level = 3

from libc.stdlib cimport malloc, free
from time import perf_counter
from random import shuffle
from os import system

cdef void bubble_sort(int* array, int size):
    cdef:
        bint swapped = True
        int i

    while swapped:
        swapped = False  # Se fizer um passe sem mudar nada, está em ordem.

        for i in range(1, size):
            if array[i] < array[i - 1]:  # Se usar i + 1 vai dar IndexError.
                array[i], array[i - 1] = array[i - 1], array[i]
                swapped = True

cpdef float get_perf(py_size: int, py_amount: int, verbose: bool):
    cdef:
        int cy_size = <int> py_size
        int cy_amount = <int> py_amount
        bint cy_verbose = <bint> verbose
        int* array = <int*> malloc(sizeof(int) * cy_size)
        float worst_case, best_case, elapsed_time
        float total_time = 0.0
        int i, j

    py_list = list(range(cy_size))

    for i in range(cy_amount):
        shuffle(py_list)
        for j in range(cy_size): array[j] = <int> py_list[j] 

        start_time = <float> perf_counter()
        bubble_sort(array, cy_size)
        end_time = <float> perf_counter()

        elapsed_time = end_time - start_time

        if i == 0:
            worst_case, best_case = elapsed_time, elapsed_time
        
        elif elapsed_time > worst_case:
            worst_case = elapsed_time
        
        elif elapsed_time < best_case:
            best_case = elapsed_time
        
        total_time += elapsed_time
    
    mean_time = total_time / cy_amount

    free(array)

    if cy_verbose:
        system('cls')
        print((f"""Analysis of time taken to sort {cy_amount} lists of size {cy_size}.
        Mean time: {mean_time:.2f} seconds.
        Best case scenario: {best_case:.2f} seconds.
        Worst case scenario: {worst_case:.2f} seconds."""))

    return mean_time
