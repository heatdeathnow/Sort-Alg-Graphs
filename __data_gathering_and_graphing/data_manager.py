from os.path import exists, join, isdir, isfile
from os import mkdir, chdir, getcwd
import pandas as pd
import utils as u
import numpy as np

# How many standard deviations an entry is allowed to deviate from the mean.
Z_SCORE = 2.0
AD_INFINITUM = True # If true, keep smiting the outliers until there are no more after the removals.

TO_SMITE = [
    'Pythonic Merge Sort', 'Efficient Merge Sort',
]

class DataManager:
    
    def __init__(self, file_name: str | None = None) -> None:
        self.__file_name = None

        if file_name is not None:
            self.file_name = file_name
            
    @property
    def file_name(self) -> str:
        return self.__file_name

    @file_name.setter
    def file_name(self, __value: str) -> None:
        
        if u.WORKING_DIRECTORY not in getcwd():
            chdir(u.WORKING_DIRECTORY)

        if '.csv' not in __value.lower():
            __value = u.format_name(__value, 'csv')

        if exists(__value):
            self.__file_name = __value
        
        elif exists(dir := join(u.DATA_DIR, __value)):
            self.__file_name = dir

        elif isdir(u.DATA_DIR):
            print(f'File {__value} does not exist. Creating it.')
            open(dir := join(u.DATA_DIR, __value), 'x').close()
            self.__file_name = dir

        else:
            print(f'File {__value} and directory {u.DATA_DIR} do not exist. Creating them.')
            mkdir(u.DATA_DIR)
            open(dir := join(u.DATA_DIR, __value), 'x').close()
            self.__file_name = dir
    
    def load_csv(self) -> None:
        self.file_df = pd.read_csv(self.file_name, sep = ';')

    def load_data(self, array: np.ndarray[float], start: int, end: int, step: int) -> None:
        data: dict[int, float] = {}

        for i, col in enumerate(range(start, end + step, step)):
            data[col] = array[i]
        
        self.data_df = pd.DataFrame(data, columns = data.keys(), index = [0])

    def get_col_order(self) -> list[str]:
        cols = list(self.file_df.columns)
        cols.sort(key = lambda col: int(col))
        
        return cols

    def merge_data(self) -> None:
        try:
            self.load_csv()

        except pd.errors.EmptyDataError:
            self.file_df = self.data_df
            return

        last_row = len(self.file_df.index)

        for col in self.data_df.columns:
            self.file_df.loc[last_row, str(col)] = self.data_df.loc[0, col]

        self.file_df = self.file_df[self.get_col_order()]

    def get_points(self, start: int, end: int) -> dict[int, float]:
        points: dict[int, float] = {}

        for col in self.file_df.columns:
            if start <= int(col) <= end:
                points[int(col)] = self.file_df[col].mean(skipna = True)
        
        return points
    
    def save(self) -> None:
        try:
            self.file_df.to_csv(self.file_name, sep = ';', index = False)
        
        except AttributeError:
            self.data_df.to_csv(self.file_name, sep = ';', index = False)

    def smite_outliners(self, z_score: float) -> int:
        last_row = len(self.file_df.index)
        removed = 0
        
        for col in self.file_df.columns:
            mean = self.file_df[col].mean(skipna = True)
            sdt = self.file_df[col].std(skipna = True)

            lower_bound = max(mean - (sdt * z_score), 0)
            upper_bound = mean + (sdt * z_score)
            
            if pd.isna(sdt):
                continue

            for i in range(last_row):
                value = self.file_df.loc[i, col]

                if pd.isna(value):
                    continue
                
                if not lower_bound < value < upper_bound:
                    self.file_df.loc[i, col] = None
                    removed += 1
        
        return removed

if __name__ == '__main__':
    if u.WORKING_DIRECTORY not in getcwd():
        chdir(u.WORKING_DIRECTORY) 

    files = list(map(lambda x: u.format_name(x, '.csv'), TO_SMITE))
    data = DataManager()

    has_removed = True
    while has_removed:

        has_removed = False
        for i, file in enumerate(files):
            if not isfile(join(u.DATA_DIR, file)): continue

            data.file_name = file
            data.load_csv()
            
            removed = data.smite_outliners(Z_SCORE)
            if removed > 0:
                print(f'{TO_SMITE[i]}: {removed} outliers removed.')
                data.save()
                has_removed = True
        
        if not AD_INFINITUM: 
            break
        