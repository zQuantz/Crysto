from enum import Enum

class ResampleFrequency(Enum):
    _1MIN = '1T'
    _5MIN = '5T'
    _10MIN = '10T'
    _15MIN = '15T'
    _20MIN = '20T'
    _30MIN = '30T'
    _60MIN = '60T'
    _1HOUR = '1H'
    _2HOUR = '2H'
    _4HOUR = '4H'
    _8HOUR = '8H'
    _1DAY = '1D'