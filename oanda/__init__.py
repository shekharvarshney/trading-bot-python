USERNAME="cvarshney"
LIVE = 'LIVE'
URL_TRADING = "url_trading"
URL_STREAM = "url_streaming"
DEFAULT_ACC = "default_account"
TOKEN = "token"
ACTIVE_ENV = LIVE
OANDA_ENV = {LIVE:{
    URL_TRADING:"api-fxtrade.oanda.com", 
    TOKEN:"SECRET",
    URL_STREAM:"stream-fxtrade.oanda.com", DEFAULT_ACC: 764454}}

CURRENCY_PAIR_SEP="_"

def default_account() -> int:
    return OANDA_ENV[ACTIVE_ENV][DEFAULT_ACC]

def split_currency_pair(currency_pair) -> list:
    return currency_pair.split('_')


