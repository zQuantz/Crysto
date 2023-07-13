from typing import Callable
import pandas as pd

from features.feature import Feature

class GenericFeature(Feature):


    def __init__(self, name: str, operation: Callable):

        self.name = name
        self.__operation = operation


    def initialize(self, data: pd.DataFrame):

        self.__feature = self.__operation(data)
        return self.__feature