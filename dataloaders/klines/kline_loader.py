import pandas as pd
import sys
sys.path.append(".")

from dataloaders.klines._constants import KLines
from dataloaders.dataloader import DataLoader
from _shared import DATA_DIR

class KLineLoader(DataLoader):

    def load(kline: KLines):
        return pd.read_csv((DATA_DIR / kline.value).with_suffix(".csv")) 

if __name__ == '__main__':

    df = KLineLoader.load(KLines.AAVEUSDT)
    print(df)