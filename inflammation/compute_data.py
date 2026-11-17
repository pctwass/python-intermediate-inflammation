"""Module containing mechanism for calculating standard deviation between datasets.
"""

import numpy as np

from inflammation import models, views
from inflammation.data_loading import CSVDataLoader


def analyse_data(data_loader: CSVDataLoader):
    """
    Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means.
    
    :param data_dir: Path to data directory
    """
    data = data_loader.load_inflammation_csv()
    daily_std = compute_daily_std(data)
    visualize_daily_std(daily_std)


def compute_daily_std(data: np.ndarray[float]) -> np.ndarray[float]:
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))
    return np.std(means_by_day_matrix, axis=0)


def visualize_daily_std(daily_std: np.ndarray[float]):
    graph_data = {
        'standard deviation by day': daily_std,
    }
    views.visualize(graph_data)