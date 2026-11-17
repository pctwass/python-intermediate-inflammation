import os
import glob
import numpy as np

from inflammation import models


class DataLoader():
    def __init__(self, data_dir_path: str, file_prefix: str = None):
        self.data_dir_path = data_dir_path
        self.file_prefix = file_prefix
        self.file_extension = None


    def get_data_file_paths(self) -> list[np.ndarray[float]]:
        if self.file_extension == None:
            raise Exception(f"A file type should be defined to load in data.")

        data_file_paths = glob.glob(os.path.join(self.data_dir_path, f'{self.file_prefix}*.{self.file_extension}'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data files found in path {self.data_dir_path} with prefix {self.file_prefix} and extension .{self.file_extension}.")

        return data_file_paths


class CSVDataLoader(DataLoader):
    def __init__(self, data_dir_path: str, file_prefix: str = None):
        super().__init__(data_dir_path, file_prefix)
        self.file_extension = 'csv'

    def load_inflammation_data(self) -> list[np.ndarray[float]]:
        data_file_paths = self.get_data_file_paths()
        inflimmation_data = map(models.load_csv, data_file_paths)
        return list(inflimmation_data)


class JSONDataLoader(DataLoader):
    def __init__(self, data_dir_path: str, file_prefix: str = None):
        super().__init__(data_dir_path, file_prefix)
        self.file_extension = 'json'

    def load_inflammation_data(self) -> list[np.ndarray[float]]:
        data_file_paths = self.get_data_file_paths()
        inflimmation_data = map(models.load_json, data_file_paths)
        return list(inflimmation_data)
    