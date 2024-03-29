# Tradingview-Binance auto trade

by TradeSabuy

Youtube : [TradeSabuy Youtube Channel](https://www.youtube.com/c/TradeSabuy)

Line ID : [@TradeSabuy](https://line.me/R/ti/p/@tradesabuy)

Register Tradingview : [Regist Here](https://th.tradingview.com/gopro/?share_your_love=shyStork66653)

This is sample code of Webhook API for TradingView to Binance API.
Do not use this source code for any comercial na krub.

Library for PythonBinance API : [Python binance documentary](https://python-binance.readthedocs.io/en/latest/)

---

### Link address to access

Example To make order : https://tradingview-binance-xyzxyzxyz-as.a.run.app/future_trade


| format address       | description                                |
| ---------------------- | -------------------------------------------- |
| .../portfolio_test   | to see Binance (TESTNET) portfolio balance |
| .../portfolio_actual | to see Binance (Actual) portfolio balance  |
| .../future_trade     | to run auto-trade with below format data   |

### Format data in TradingView Alert

```bash
{
	"system": "Long and Short future",
	"passphrase": "tradesabuy_binance_autotrade",
	"time": "{{timenow}}",
	"actual_trade": "no",
	"QTY_Type": "FINAL",
	"exchange": "{{exchange}}",
	"ticker": "{{ticker}}",
	"bar": {
		"time": "{{time}}",
		"open": {{open}},
		"high": {{high}},
		"low": {{low}},
		"close": {{close}},
		"volume": {{volume}}
	},
	"strategy": {
		"SIDE": "BUY",
		"QTY": "5%",
		"LEVERAGE": "1"
	}
}
```

---

### Format data for testing

```bash
{
	"system": "Long and Short future",
	"passphrase": "tradesabuy_binance_autotrade",
	"time": "22 Jan 2023",
	"actual_trade": "no",
	"QTY_Type": "FINAL",
	"exchange": "Binance",
	"ticker": "BTCUSDT",
	"bar": {
		"time": "9:00",
		"open": 10000,
		"high": 12000,
		"low": 8000,
		"close": 11000,
		"volume": 100
	},
	"strategy": {
		"SIDE": "BUY",
		"QTY": "5%",
		"LEVERAGE": "1"
	}
}
```

---

### Actual Trade type


| Name         | Example             | Description                                                                                                     |
| -------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------- |
| actual_trade | "YES" or any        | If not "YES", will make trade in Binance testnet, not actual Binance Exchange                                   |
| QTY_Type     | "FINAL" or "ACTUAL" | If "FINAL", input QTY will be final quantity type.<br />If "ACTUAL", input QTY will be number of order sending. |

### Strategy type of order


| Name     | Example                      | Description                                                                                   |
| ---------- | ------------------------------ | ----------------------------------------------------------------------------------------------- |
| SIDE     | "BUY" or "SELL"              | Specific preferred FINAL side of product                                                      |
| QTY      | "5"<br />"5%"<br />"100USDT" | Specific preferred FINAL qty (In units, percentage of portfolio or amount of USDT) of product |
| LEVERAGE | "1"                          | Set leverage order                                                                            |

---

### API key

To use this automatic bot, add you API key to config.py file.
