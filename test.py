import pandas as pd

from dataloaders.klines.kline_loader import KLineLoader
from dataloaders.klines._constants import KLineReference
from dataloaders.klines._constants import KLines

from processors._constants import ResampleFrequency
from common.instrument import Instrument

from features.two_candle_close import TwoCandleClose
from features.generic_feature import GenericFeature
from features.rolling_feature import RollingFeature

if __name__ == '__main__':

    loader = KLineLoader(KLines.BTCUSDT, ResampleFrequency._5MIN, KLineReference.OPEN_TIME)
    features = [
        RollingFeature('_8_low', operation=pd.Series.mean, n_periods=8, reference_column='low'),
        RollingFeature('_10_high', operation=pd.Series.mean, n_periods=10, reference_column='high'),
        TwoCandleClose(n_periods_low=8, n_periods_high=10),
        GenericFeature('body_proportion', operation=lambda x: abs(x.close - x.open) / (x.high - x.low)),
        RollingFeature('candle_size_z', operation=lambda x: abs(x.values[-1] - x.mean()) / x.std(), n_periods=20, reference_column='close')
    ]
    instrument = Instrument(uid=KLines.BTCUSDT.value, price_loader=loader, features=features)
    print(instrument.data)
    instrument.data.to_csv("tmp/btc.csv", index=False)
