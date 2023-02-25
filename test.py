from dataloaders.klines.kline_loader import KLineLoader
from dataloaders.klines._constants import KLineReference
from dataloaders.klines._constants import KLines

from processors._constants import ResampleFrequency
from common.instrument import Instrument


if __name__ == '__main__':

    loader = KLineLoader(KLines.BTCUSDT, ResampleFrequency._5MIN, KLineReference.OPEN_TIME)
    instrument = Instrument(uid=KLines.BTCUSDT.value, price_loader=loader)
    print(instrument.price_data)
