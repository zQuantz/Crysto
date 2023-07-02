from typing import Callable
import pandas as pd

from features.feature import Feature

class RollingFeature(Feature):


    def __init__(self, name: str, operation: Callable, n_periods: int, reference_column: str):

        self.name = name
        self.__n_periods = n_periods
        self.__operation = operation
        self.__reference_column = reference_column


    def initialize(self, data: pd.DataFrame):
        
        self.__feature = data[self.__reference_column].rolling(self.__n_periods).apply(self.__operation)
        return self.__feature