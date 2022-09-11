# Tradingview-Binance auto trade

by TradeSabuy

Youtube : [TradeSabuy Youtube Channel](https://www.youtube.com/c/TradeSabuy)

Line ID : [@TradeSabuy](https://line.me/R/ti/p/@tradesabuy)

Register Tradingview : [Regist Here](https://th.tradingview.com/gopro/?share_your_love=shyStork66653)

This is sample code of Webhook API from TradingView to Binance API.
Do not use this source code for any comercial na krub.

Library for PythonBinance API : [Python binance documentary](https://python-binance.readthedocs.io/en/latest/)

---

### Link address to access

Example To make order : https://tradingview-binance-xyzxyzxyz-as.a.run.app/**future_trade**


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

### Actual Trade type


| Name         | Example      | Description                                                                   |
| -------------- | -------------- | ------------------------------------------------------------------------------- |
| actual_trade | "YES" or any | if not "YES", will make trade in Binance testnet, not actual Binance Exchange |

### Strategy type of order


| Name     | Example         | Description                                                                   |
| ---------- | ----------------- | ------------------------------------------------------------------------------- |
| SIDE     | "BUY" or "SELL" | Specific preferred FINAL sideof product                                       |
| QTY      | "5" or "5%"     | Specific preferred FINAL qty (In units or percentage of portfolio) of product |
| LEVERAGE | "1"             | Set leverage order                                                            |

---

### API key

To use this automatic bot, add you API key to config.py file.
