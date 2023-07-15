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


KLines = Enum('KLines',
    {
        file.stem: file.stem
        for file in DATA_DIR.iterdir()
        if file.stat().st_size > 120
        and file.suffix == '.csv'
    },
    type=str,
)

KLINE_AGGS = dict(
    open_time='first',
    open='first',
    high='max',
    low='min',
    close='last',
    volume='sum',
    close_time='last',
    quote_volume='sum',
    number_of_trades='sum',
    taker_buy_base_volume='sum',
    taker_buy_quote_volume='sum',
    ignore='last'
)

class ResampleFrequency(Enum):
    _1MIN = '1T'
    _5MIN = '5T'
    _10MIN = '10T'
    _15MIN = '15T'
    _20MIN = '20T'
    _30MIN = '30T'
    _60MIN = '60T'
    _1HOUR = '1H'
    _2HOUR = '2H'
    _4HOUR = '4H'
    _8HOUR = '8H'
    _1DAY = '1D'