import http.client
import json

USERNAME="cvarshney"
LIVE = 'LIVE'
URL_TRADING = "url_trading"
URL_STREAM = "url_streaming"
TOKEN = "token"
ACTIVE_ENV = LIVE
OANDA_ENV = {LIVE:{
    URL_TRADING:"api-fxtrade.oanda.com", 
    TOKEN:"b585d9a25841fe180735e7f7ea0ec7cd-9877e09ba5bed932130bd3ed7f4afbe7",
    URL_STREAM:"stream-fxtrade.oanda.com"}}
HTTP_GET = 'GET'
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
default_hdrs={'Content-type': 'application/json', 'Authorization':"Bearer {0}".format(OANDA_ENV[ACTIVE_ENV][TOKEN])}
def oanda_response(uri, params=None, method=HTTP_GET, headers={}):
    headers.update(default_hdrs)
    oanda_rest_conn=http.client.HTTPSConnection(OANDA_ENV[ACTIVE_ENV][URL_TRADING])
    oanda_rest_conn.request(method,uri,params,headers)
    oanda_rest_resp=oanda_rest_conn.getresponse()
    response_json=oanda_rest_resp.read()
    return json.loads(response_json.decode('UTF-8'))
