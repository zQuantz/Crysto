from abc import ABC, abstractmethod
from typing import List
import pandas as pd

from common.instrument import Instrument

class Strategy(ABC):

    def __init__(self, instruments: List[Instrument]):

        self.__instruments = instruments

    def get_entry_signals(self, data: pd.DataFrame):
        pass

    def get_exit_signals(self, data: pd.DataFrame):
        pass