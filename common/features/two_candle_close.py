import pandas as pd

from models.feature import Feature

class TwoCandleClose(Feature):

    def __init__(self, n_periods_low: int, n_periods_high: int):

        self.__n_periods_low = n_periods_low
        self.__n_periods_high = n_periods_high
        self.name = f'TwoCandleClose({n_periods_low}, {n_periods_high})'

    def initialize(self, data: pd.DataFrame):

        low_col = f"_{self.__n_periods_low}_low"
        high_col = f"_{self.__n_periods_high}_high"

        first = data.shift(periods=1)
        second = data.copy()

        # Long
        first_candle = (
            first.open.between(first[low_col], first[high_col]) 
            &
            (first.close >= first[high_col])
        )
        second_candle = (
            (second.open >= second[high_col])
            &
            (second.close >= second.open) 
        )
        long = (first_candle & second_candle).astype(int)

        # Short
        first_candle = (
            first.open.between(first[low_col], first[high_col]) 
            &
            (first.close <= first[low_col])
        )
        second_candle = (
            (second.open <= second[low_col])
            &
            (second.close <= second.open) 
        )
        short = -(first_candle & second_candle).astype(int)

        self.__feature = short + long
        return self.__feature