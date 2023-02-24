from _constants import KLINE_COLUMNS 
from _constants import SYMBOLS_URL
from _constants import ZIP_URL

from datetime import timedelta
from zipfile import BadZipFile
from datetime import datetime
from joblib import Parallel
from zipfile import ZipFile
from joblib import delayed
from pathlib import Path
from io import BytesIO
import pandas as pd
import requests
import os

import sys
sys.path.append(".")
from _shared import DATA_DIR, logger


def fetch_url(url):
    response = requests.get(url, timeout=10)
    return response


def get_all_symbols():
    response = fetch_url(SYMBOLS_URL)
    symbols = response.content.decode('utf-8').split("\n")
    symbols.remove('')
    symbols = [symbol for symbol in symbols if 'USDT ' in f"{symbol} "]
    return symbols


def download_kline_data(url):
    zip_file = Path(url.split("/")[-1])
    csv_file = zip_file.with_suffix(".csv").as_posix()
    zip_response = fetch_url(url)
    zip_data = ZipFile(BytesIO(zip_response.content))
    with zip_data.open(csv_file) as _file:
        df = pd.read_csv(_file, header=None, names=KLINE_COLUMNS)
    return df

def download_1m_kline(date, symbol):
    url = ZIP_URL.format(
        DATE=date,
        SYMBOL=symbol,
        TIMEFRAME="1m"
    )
    df = download_kline_data(url)
    df.index.name = 'open_time'
    df = df.reset_index()
    df.to_csv(DATA_DIR / f"tmp/{date}.csv", index=False)

def download_date(date, symbol):
    date = date.strftime('%Y-%m-%d')
    try:
        return download_1m_kline(date, symbol)
    except BadZipFile:
        pass    

def download_symbol(symbol: str, dates: list[datetime]):

    print(symbol)

    Parallel(n_jobs=20)(
        delayed(download_date)(
            date,
            symbol
        )
        for date in dates
    )

    dfs = []
    for file in (DATA_DIR / "tmp").iterdir():
        dfs.append(pd.read_csv(file))
        os.remove(file)
    
    if len(dfs) > 0:
        df = pd.concat(dfs).sort_values('open_time', ascending=True)
        logger.info(f"Collected {len(df)} rows for {symbol}")
    else:
        df = pd.DataFrame(columns=KLINE_COLUMNS)
        logger.warning(f"No data collected for {symbol}")

    df.to_csv(DATA_DIR / f"{symbol}.csv", index=False)

def main():

    dates = pd.date_range(
        start=datetime(2021, 3, 1),
        end=datetime.now() - timedelta(days=1),
        freq="D"
    )
    
    for file in (DATA_DIR / "tmp").iterdir():
        os.remove(file)
    
    for symbol in get_all_symbols():
        if (DATA_DIR / f"{symbol}.csv").exists():
            continue
        logger.info(f"Collecting {symbol}")
        download_symbol(symbol, dates)

if __name__ == '__main__':
    main()