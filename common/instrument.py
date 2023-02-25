import sys
sys.path.append(".")

from dataloaders.dataloader import DataLoader

class Instrument:

    def __init__(self, uid: str, price_loader: DataLoader):
        
        self.uid = uid
        self.price_data = price_loader.load()