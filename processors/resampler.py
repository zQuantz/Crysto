import pandas as pd

import sys
sys.path.append(".")

from processors._constants import ResampleFrequency

class Resampler:

    def resample(
        self, 
        frequency: ResampleFrequency | None,
        on_column: str | None,
        data: pd.DataFrame,
        aggregations: dict
    ) -> pd.DataFrame:
        if not frequency:
            return data
        return data.resample(frequency.value, on=on_column).agg(aggregations)