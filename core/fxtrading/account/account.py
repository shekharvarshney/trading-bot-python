from typing import TypeVar,Generic
from builtins import str,float,int
from core import attributesFromDict
T = TypeVar('T')

class Account(Generic[T]):
    
    def __init__(self, total_balance:float,  margin_available:float, currency:str, 
                 account_id: T,margin_rate: float, unrealised_pnl:float=0.0, realised_pnl:float=0.0, 
                 margin_used:float=0.0,open_trades:int=0) -> None:
        attributesFromDict(locals())
