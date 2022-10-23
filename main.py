import json, math, config
import os
import requests

from flask import Flask, request
from binance.client import Client
from binance.enums import *

app = Flask(__name__)

def round_decimals_down(number:float, decimals:int=2):
    """
    Returns a value rounded down to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.floor(number)

    factor = 10 ** decimals
    return math.floor(number * factor) / factor

def get_existing_amount(symbol, client):
    i = float(client.futures_position_information(symbol = symbol)[-1]['positionAmt'])
    return i

def get_cash(client):
    item = client.futures_account()
    balance = float(item['totalMarginBalance']) #all balance
    cash = float(item['totalCrossWalletBalance']) - float(item['totalInitialMargin']) #cross wallet balance - all margin
    return balance, cash

def trade_order(symbol, side, qty, client):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            positionSide='BOTH',
            type='MARKET',
            quantity=qty
            )
        return {
            'status': "Success",
            'message' : format(order)
        }
    except Exception as e:
        return {
            'status': 'False',
            'message': format(e)
            }

@app.route('/')
def helloworld():
    return 'This is sample of Tradingview-Binance auto trade by TradeSabuy.'

@app.route('/portfolio_actual')
def portfolio_actual():
    try:
        client = Client(config.API_KEY_future, config.API_SECRET_future, tld='com')
        return format(client.futures_account_balance())
    except:
        return 'Cannot access API ACTUAL port'

@app.route('/portfolio_test')
def portfolio_test():  
    try:
        client = Client(config.API_KEY_test, config.API_SECRET_test, tld='com')
        client.FUTURES_URL  = config.testnet_URL
        return format(client.futures_account_balance())
    except:
        return 'Cannot access API TEST port'

@app.route('/test', methods=['POST'])
def test():
    print(request.data)
    return {
        'code': 'success'
    }

@app.route('/future_trade', methods=['POST'])
def future_trade():
    # check Data Format
    try:
        data = json.loads(request.data)
        symbol = data["ticker"]
        strategy = data['strategy']
        side = strategy['SIDE'].upper()
    except Exception as e:
        return {
            'status': 'Wrong format data',
            'message': format(e)
            }

    # check Pass phrase
    if data['passphrase'] != config.WEBHOOK_PASSPHRASE:
        return {
            "code": "error",
            "message": "Invalid passphrase"
        }

    # check TEST or ACTUAL trade
    if data['actual_trade'].upper() == "YES":
        client = Client(config.API_KEY_future, config.API_SECRET_future, tld='com')
    else:
        client = Client(config.API_KEY_test, config.API_SECRET_test, tld='com')
        client.FUTURES_URL  = config.testnet_URL

    # Set leverage
    try:
        leverage_setup = round(float(strategy['LEVERAGE']))
    except:
        leverage_setup = 1
    client.futures_change_leverage(symbol = symbol, leverage = leverage_setup)

    # check qty type (Percentage or unit)
    if strategy['QTY'][-1] == "%":
        percentage_port_require = float(strategy['QTY'][:-1])/100
        URL = config.URL + symbol.upper()
        last_price = float(requests.get(URL).json()['lastPrice'])
        require_qty_raw = get_cash(client)[0] * percentage_port_require / last_price
    elif 'USDT' in strategy['QTY']:
        URL = config.URL + symbol.upper()
        last_price = float(requests.get(URL).json()['lastPrice'])
        require_qty_raw = float(strategy['QTY'][:-4]) / last_price
    else:
        require_qty_raw = float(strategy['QTY'])
        
    # Round Decimal of symbol
    for i in client.futures_exchange_info()["symbols"]:
        if i['symbol'] == symbol:
            precision =  int(i['quantityPrecision'])
            break
    require_qty = round_decimals_down(require_qty_raw, precision)
    if side == "SELL":
        require_qty = -require_qty

    # make order
    try:
        QuantityType = data["QTY_Type"].upper()
    except:
        QuantityType = "ACTUAL"
    
    if QuantityType == "FINAL":
        action_amount = require_qty - get_existing_amount(symbol, client)
        action_amount = round_decimals_down(action_amount, precision)
        if action_amount > 0:
            order = trade_order(symbol, "BUY", abs(action_amount), client)
        elif action_amount < 0:
            order = trade_order(symbol, "SELL", abs(action_amount), client)
        else:
            order = trade_order(symbol, side, abs(action_amount), client)
    else:
        order = trade_order(symbol, side, abs(require_qty), client)
        
    return(order)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))