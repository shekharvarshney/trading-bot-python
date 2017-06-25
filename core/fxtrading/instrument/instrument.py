from core import attributesFromDict
from typing import TypeVar, Generic
from builtins import str, float, int

T = TypeVar('T')


class InstrumentPairInterestRate:

    def __init__(self, base_currency_bid_interest_rate: float=None, base_currency_ask_interest_rate: float=None,
                 quote_currency_bid_interest_rate: float=None, quote_currency_ask_interest_rate: float=None):
        attributesFromDict(locals())


class TradeableInstrument(Generic[T]):

    def __init__(self, instrument: str, instrument_id: T=None, pip: float=None, description: str=None,
                 instrument_pair_interest_rate: InstrumentPairInterestRate=None):
        attributesFromDict(locals())

    def __hash__(self):
        return hash(self.instrument, self.instrument_id)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.instrument == self.instrument and other.instrument_id == self.instrument_id
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        else:
            return NotImplemented

