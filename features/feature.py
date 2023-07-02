from abc import ABC, abstractmethod
import pandas as pd


class Feature(ABC):

    @abstractmethod
    def initialize(self, data: pd.DataFrame):
        pass