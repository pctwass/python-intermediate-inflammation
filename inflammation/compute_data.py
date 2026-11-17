"""Module containing mechanism for calculating standard deviation between datasets.
"""

from inflammation.models import compute_daily_std
from inflammation.views import visualize_daily_std
from inflammation.data_loading import CSVDataLoader


def analyse_data(data_loader: CSVDataLoader):
    """
    Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means.
    
    :param data_dir: Path to data directory
    """
    data = data_loader.load_inflammation_data()
    daily_std = compute_daily_std(data)
    return daily_std
    visualize_daily_std(daily_std)