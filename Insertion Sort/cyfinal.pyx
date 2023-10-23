#cython: language_level = 3

from libc.stdlib cimport malloc, free
from time import perf_counter
from random import shuffle
from os import system

cdef void insertion_sort(int* to_sort, int size):
    cdef: 
        int i
        int j

    for i in range(size):
        j = i

        while j > 0 and to_sort[j - 1] > to_sort[j]:  # while there is still stuff and the stuff immediatelly to the left is bigger...
            to_sort[j - 1], to_sort[j] = to_sort[j], to_sort[j - 1]  # Swap the item at current index with the item to the left.
            j -= 1

cpdef float get_perf(int py_size, int py_amount, verbose: bool):
    cdef:
        int cy_size = <int> py_size
        int cy_amount = <int> py_amount
        bint cy_verbose = <bint> verbose
        int* array = <int*> malloc(cy_size * sizeof(int))  # This will be passed instead, cause it's a C-Array with C-Integers.
        float best_case, worst_case, elapsed_time
        float total_time = 0.0
        int i, j

    py_list = list(range(cy_size))  # This is just so I can use Python's shuffle function

    for i in range(cy_amount):
        shuffle(py_list)
        for j in range(cy_size): array[j] = <int> py_list[j]  # Converts all the Python integer objects into C-ints.

        start_time = <float> perf_counter()
        insertion_sort(array, cy_size)
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
