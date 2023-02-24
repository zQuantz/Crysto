from enum import Enum

import sys
sys.path.append(".")
from _shared import DATA_DIR

class KLineReference(Enum):

    OPEN_TIME = 'open_time'
    CLOSE_TIME = 'close_time'
    OPEN_PRICE = 'open'
    HIGH_PRICE = 'high'
    LOW_PRICE = 'low'
    CLOSE_PRICE = 'close'
    VOLUME = 'volume'
    QUOTE_ASSET_VOLUME = 'quote_volume'
    NUMBER_OF_TRADES = 'number_of_trades'


KLines: Enum = Enum('KLines', 
    {
        file.stem: file.stem
        for file in DATA_DIR.iterdir()
        if file.stat().st_size > 120
        and file.suffix == '.csv'
    }
)