from enum import Enum

class ObservationType(Enum):
    INFO_COST   = 239
    INFO_USE    = 240
    TOTALCOST   = 53
    
class ValueUnit(Enum):
    VOLUME      = 93

class CostUnit(Enum):
    BRL       = 112
    VALUES    = 12