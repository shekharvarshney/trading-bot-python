import http.client
import json

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
HTTP_GET = 'GET'

## OANDA JSON KEYS START
accounts = "accounts";
account_id = "accountId";
account_currency = "accountCurrency";
margin_rate = "marginRate";
margin_used = "marginUsed";
margin_avail = "marginAvail";
balance = "balance";
unrealized_pl = "unrealizedPl";
realized_pl = "realizedPl";
open_trades = "openTrades";
instruments = "instruments";
instrument = "instrument";
interest_rate = "interestRate";
disconnect = "disconnect";
pip = "pip";
bid = "bid";
ask = "ask";
heartbeat = "heartbeat";
candles = "candles";
code = "code";
open_mid = "openMid";
high_mid = "highMid";
low_mid = "lowMid";
close_mid = "closeMid";
time = "time";
tick = "tick";
prices = "prices";
trades = "trades";
trade_id = "tradeId";
price = "price";
avg_price = "avgPrice";
id = "id";
stop_loss = "stopLoss";
take_profit = "takeProfit";
units = "units";
side = "side";
type = "type";
orders = "orders";
order_id = "orderId";
positions = "positions";
expiry = "expiry";
trade_opened = "tradeOpened";
order_opened = "orderOpened";
transaction = "transaction";
pl = "pl";
interest = "interest";
account_balance = "accountBalance";
## OANDA JSON KEYS END

default_hdrs={'Content-type': 'application/json', 'Authorization':"Bearer {0}".format(OANDA_ENV[ACTIVE_ENV][TOKEN])}
CURRENCY_PAIR_SEP="_"

def default_account() -> int:
    return OANDA_ENV[ACTIVE_ENV][DEFAULT_ACC]

def split_currency_pair(currency_pair) -> list:
    return currency_pair.split('_')

def oanda_response(uri:str, params:dict=None, method:str=HTTP_GET, headers:dict={}):
    headers.update(default_hdrs)
    oanda_rest_conn=http.client.HTTPSConnection(OANDA_ENV[ACTIVE_ENV][URL_TRADING])
    oanda_rest_conn.request(method,uri,params,headers)
    oanda_rest_resp=oanda_rest_conn.getresponse()
    response_json=oanda_rest_resp.read()
    return json.loads(response_json.decode('UTF-8'))
