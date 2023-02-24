ZIP_URL = "https://data.binance.vision/data/spot/daily/klines/{SYMBOL}/{TIMEFRAME}/{SYMBOL}-{TIMEFRAME}-{DATE}.zip"
SYMBOLS_URL = "https://raw.githubusercontent.com/binance/binance-public-data/master/data/symbols.txt"
KLINE_COLUMNS = [
    'open',
    'high',
    'low',
    'close',
    'volume',
    'close_time',
    'quote_volume',
    'number_of_trades',
    'taker_buy_base_volume',
    'taker_buy_quote_volume',
    'ignore'
]

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