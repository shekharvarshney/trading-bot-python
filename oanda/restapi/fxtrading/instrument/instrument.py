from builtins import str
from core.fxtrading.instrument.instrument import TradeableInstrument,InstrumentPairInterestRate
from typing import List
from core.fxtrading.instrument.iinstrument_data_provider import InstrumentDataProvider
from oanda.restapi.fxtrading.instrument import INSTRUMENTS_RESOURCE, fields_requested
from oanda import default_account, split_currency_pair
from oanda.restapi import  oanda_response, interest_rate, instrument, pip,bid,ask, instruments


class OandaInstrumentDataProviderService(InstrumentDataProvider[str]):

    def get_instruments(self) -> List[TradeableInstrument[str]]:
        uri="{0}?accountId={1}&fields={2}".format(INSTRUMENTS_RESOURCE, default_account(), fields_requested)
        instrument_data = oanda_response(uri)
        instr_array=[]
        for instr in instrument_data[instruments]:
            currency_pair = split_currency_pair(instr[instrument])
            base_ccy = currency_pair[0]
            quote_ccy = currency_pair[1]
            interest_rate_dict = instr[interest_rate]
            tradeable_instrument=TradeableInstrument(instr[instrument],instr[instrument],instr[pip], None,
                                                     InstrumentPairInterestRate(interest_rate_dict[base_ccy][bid],
                                                                                interest_rate_dict[base_ccy][ask],
                                                                                interest_rate_dict[quote_ccy][bid],
                                                                                interest_rate_dict[quote_ccy][ask]))
            instr_array.append(tradeable_instrument)
        return instr_array