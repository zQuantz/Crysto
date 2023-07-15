from dataclasses import dataclass

@dataclass
class Trade:

    ticker: str
    size: int
    price: float
    direction: 1 | -1