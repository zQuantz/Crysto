from abc import ABC, abstractmethod
from enum import Enum

class DataLoader(ABC):

    @abstractmethod
    def load(data: Enum):
        pass

    