from data_manager import DataManager
import matplotlib.pyplot as plt
from os import chdir, getcwd
from os.path import join
import utils as u

ALGORITHMS = ('Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort')
START = 0
END = 500000
DPI = 300

TITLE = 'Sorting Algorithms'
FILE_NAME = None and join(u.GRAPH_DIR, 'pythonic_v_efficient.png')

CUSTOM_LABELS = [
    
]

if __name__ == '__main__':
    cwd = getcwd()

    if u.WORKING_DIRECTORY not in cwd:
        chdir(u.WORKING_DIRECTORY)

    if not isinstance(ALGORITHMS, tuple):
        raise TypeError('Format the ALGORITHMS constant properly.')

    if len(ALGORITHMS) < 1:
        raise ValueError('No algorithms provided.')
    
    png_files = list(map(lambda alg: join(u.GRAPH_DIR, u.format_name(alg, 'png')), ALGORITHMS))
    formatted_names = list(map(lambda alg: u.format_name(alg), ALGORITHMS))
    
    plt.xlabel('Size')
    plt.ylabel('Time')

    if len(ALGORITHMS) < 2:
        data = DataManager(ALGORITHMS[0])
        data.load_csv()
        points = data.get_points(START, END)

        plt.plot(points.keys(), points.values())
        plt.suptitle(TITLE if TITLE else ALGORITHMS[0])
        plt.savefig(FILE_NAME if FILE_NAME is not None else png_files[0], dpi = DPI)

    else:
        data = DataManager()

        for i, sort in enumerate(ALGORITHMS):
            data.file_name = sort
            data.load_csv()
            points = data.get_points(START, END)

            plt.plot(points.keys(), points.values(), label = CUSTOM_LABELS[i] if len(CUSTOM_LABELS) >= len(ALGORITHMS) else ALGORITHMS[i])
        
        plt.legend()
        plt.suptitle(TITLE if TITLE is not None else ' | '.join(ALGORITHMS))
        plt.savefig(FILE_NAME if FILE_NAME is not None else join(u.GRAPH_DIR, ' '.join(formatted_names) + '.png'), dpi = DPI)
