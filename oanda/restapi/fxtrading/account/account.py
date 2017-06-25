from core.fxtrading.account.iaccount_data_provider import AccountDataProvider
from builtins import int
from core.fxtrading.account.account import Account
from typing import List
from oanda.restapi.fxtrading.account import ACCOUNTS_RESOURCE
from oanda import oanda_response, balance, \
    margin_avail, account_currency, margin_rate, unrealized_pl, realized_pl, \
    margin_used, open_trades, USERNAME, account_id, accounts


class OandaAccountDataProviderService(AccountDataProvider[int]):
    
    def get_account_info(self, account_id:int) -> Account[int]:
        uri = "{0}/{1}".format(ACCOUNTS_RESOURCE, account_id)
        account_data = oanda_response(uri)
        return Account(account_data[balance], account_data[margin_avail], account_data[account_currency], account_id,
                       account_data[margin_rate], account_data[unrealized_pl], account_data[realized_pl],
                       account_data[margin_used], account_data[open_trades])
    
    def get_accounts_info(self) -> List[Account[int]]:
        uri = "{0}?username={1}".format(ACCOUNTS_RESOURCE, USERNAME)
        all_account_data=oanda_response(uri)
        return [self.get_account_info(acc[account_id]) for acc in all_account_data[accounts]]
