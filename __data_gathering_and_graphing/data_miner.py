from data_manager import DataManager
from os import system, getcwd, chdir
from importlib import import_module
from os.path import exists, join
from tqdm import tqdm
import numpy as np
import utils as v

SORT_NAMES = ('Merge Sort',)
RUNS = 15

START_SIZE = 500000
STEP = 1000
MAX_SIZE = 1000000

ITERATIONS = (MAX_SIZE + STEP - START_SIZE) // STEP


def clear() -> None:
    system('cls')

def gather_data() -> None:
    for rep in range(RUNS):

        array = np.empty(ITERATIONS, float)
        data = DataManager()

        for sort in SORT_NAMES:
            module_name = v.format_name(sort)
            sort_alg = import_module(module_name)
            
            for i, list_size in enumerate(range(START_SIZE, MAX_SIZE + STEP, STEP)):
                time_taken: float = sort_alg.get_perf(list_size, 1, False)
                array[i] = time_taken
                progress_bar = tqdm.format_meter((list_size - START_SIZE) / STEP,
                                                 (MAX_SIZE - START_SIZE) / STEP,
                                                 0, ncols = 50, bar_format = '{bar}| {percentage:.2f}%')
                
                clear()
                print(f"""Gathering performance data for {f'{', '.join(SORT_NAMES)}' if len(SORT_NAMES) > 1 else sort}
    {f'Current sort: {sort}' if len(SORT_NAMES) > 1 else ''}
    {f'Progress: {progress_bar}' if list_size < MAX_SIZE else 'Data gathering complete.'}

    Current list size: {f'{list_size + STEP}' if list_size < MAX_SIZE else f'{list_size}'}
    Mean time taken to sort lists of size {list_size}: {time_taken:.2f} seconds.

    Initial list size: {START_SIZE}
    Max/Final list size: {MAX_SIZE}

    {'' if SORT_NAMES.index(sort) + 1 == len(SORT_NAMES) or len(SORT_NAMES) < 2 else f'Next up {SORT_NAMES[SORT_NAMES.index(sort) + 1]}'}
    Runs left: {RUNS - rep - 1}""")

            data.file_name = sort
            data.load_data(array, START_SIZE, MAX_SIZE, STEP)
            data.merge_data()
            data.save()

if __name__ == '__main__':
    if (RUNS < 1 or len(SORT_NAMES) < 1):

        raise ValueError

    cwd = getcwd()
    print(cwd)
    if v.WORKING_DIRECTORY not in cwd and 'Sorting Algorithms' in cwd:
        chdir(v.WORKING_DIRECTORY)
    
    elif v.WORKING_DIRECTORY not in cwd:
        raise ValueError
    
    gather_data()
