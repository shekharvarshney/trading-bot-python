from typing import TypeVar, Generic
from builtins import str, float, int
from core import attributesFromDict
T = TypeVar('T')


class Account(Generic[T]):
    
    def __init__(self, total_balance:float, margin_available:float, currency:str,
                 account_id: T, margin_rate: float, unrealised_pnl:float=0.0, realised_pnl:float=0.0,
                 margin_used:float=0.0, open_trades:int=0) -> None:
        attributesFromDict(locals())
        
    def __hash__(self):
        return hash(self.account_id)
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.account_id == self.account_id
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        else:
            return NotImplemented