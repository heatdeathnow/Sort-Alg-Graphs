from libc.stdlib cimport malloc, free
from time import perf_counter
from random import shuffle
from os import system

cdef void merge_sort(int* to_sort, int size):
    cdef int* aux = <int*> malloc(sizeof(int) * size)
    split_and_merge(to_sort, aux, 0, size)
    free(aux)

cdef (int, int) split_and_merge(int* to_sort, int* aux, int start, int end):

    if end - start == 1:
        return start, end
    
    cdef int mid = (start + end) // 2

    start, mid = split_and_merge(to_sort, aux, start, mid)
    mid, end = split_and_merge(to_sort, aux, mid, end)

    merge_lists(to_sort, aux, start, mid, end)

    return start, end

cdef void merge_lists(int* to_sort, int* aux, int start, int mid, int end):
    cdef:
        int i = start
        int j = mid
        int k = start
    
    while i < mid and j < end:
        if to_sort[i] < to_sort[j]:
            aux[k] = to_sort[i]
            i += 1
    
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
    
    for k in range(start, end):
        to_sort[k] = aux[k]

cpdef float get_perf(int py_size, int py_amount, verbose: bool = False):
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
        merge_sort(array, cy_size)
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
