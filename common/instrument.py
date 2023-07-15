from typing import List

from models.dataloader import DataLoader
from models.feature import Feature

class Instrument:

    def __init__(self, uid: str, price_loader: DataLoader, features: List[Feature]):
        
        self.uid = uid
        self.data = price_loader.load()

        self.features = features
        self.initialize_features()

    def initialize_features(self):

        for feature in self.features:
            print("Calculating feature", feature.name)
            self.data[feature.name] = feature.initialize(self.data)