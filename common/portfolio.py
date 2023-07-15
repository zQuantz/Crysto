from typing import Dict
import numpy as np

from models.trade import Trade

class Portfolio:

    def __init__(self):
        self.positions: Dict[Trade] = {}
        pass

    def execute_trade(self, new_trade: Trade):

        if new_trade.ticker not in self.positions:
            self.positions[new_trade.ticker] = new_trade
            return
        
        existing_position = self.positions.get(new_trade.ticker)
        if new_trade.size + existing_position.size == 0:
            del self.positions[new_trade.ticker]
            return

        if new_trade.direction == existing_position.direction:
            d = new_trade.size + existing_position.size
            price = (new_trade.size / d) * new_trade.price
            price += (existing_position.size / d) * existing_position.price
            size = new_trade.size + existing_position.size
        elif new_trade.direction != existing_position.direction:
            price = existing_position.price
            size = existing_position.size - new_trade.size

        new_position = Trade(
            ticker = new_trade.ticker,
            size=size,
            price=price,
            direction=existing_position.direction
        )
        self.positions[new_position.ticker] = new_position

