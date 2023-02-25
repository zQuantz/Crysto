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