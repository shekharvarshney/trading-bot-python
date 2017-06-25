import abc
from typing import TypeVar, Generic, List
from core.fxtrading.instrument.instrument import TradeableInstrument

T = TypeVar('T')

class InstrumentDataProvider(Generic[T], metaclass=abc.ABCMeta):


    @abc.abstractmethod
    def get_instruments(self) -> List[TradeableInstrument[T]]:
        raise NotImplementedError('developers must implement get_instruments to use this base class')