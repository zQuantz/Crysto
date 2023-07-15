import pandas as pd
import sys
sys.path.append(".")

from common.resampler import ResampleFrequency
from common.resampler import Resampler

from common._constants import KLINE_AGGS
from common._constants import KLines
from models.dataloader import DataLoader
from _shared import DATA_DIR

class KLineLoader(DataLoader):

    def __init__(self, kline: KLines, frequency: ResampleFrequency | None = None, on_column: str | None = None):
        self.kline = kline
        self.frequency = frequency
        self.on_column = on_column.value

    def load(self):
        data = pd.read_csv((DATA_DIR / self.kline.value).with_suffix(".csv"))
        data[self.on_column] = pd.to_datetime(data[self.on_column], unit='ms')
        return Resampler().resample(
            frequency=self.frequency,
            on_column=self.on_column,
            data=data,
            aggregations=KLINE_AGGS
        )