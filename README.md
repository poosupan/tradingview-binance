# tradingview-binance-test

by TradeSabuy

Youtube : [Trade Sabuy Youtube Channel](https://www.youtube.com/channel/UCDkxnUHxUSrFDzchFysZ-hQ)

Line ID : [@TradeSabuy](https://lin.ee/SZ8z9Nb)

This is sample code of Webhook API from TradingView to Binance API.
Do not use this source code for any comercial na krub.

Library for PythonBinance API : [Python binance documentary](https://python-binance.readthedocs.io/en/latest/)

---

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
		"QTY": "50%",
		"LEVERAGE": "1"
	}
}
```

---

### Strategy type of order


| Name           | Example         | Description                                                        |
| :--------------- | ----------------- | -------------------------------------------------------------------- |
| SIDE           | "BUY" or "SELL" | Specific**final** sideof product                                   |
| QTY            | "5" or "5%"     | Specific**final** qty (In unit or percentage portfolio) of product |
| <br />LEVERAGE | "1"             | Set leverage order                                                 |

---

### API key

To use this automatic bot, add you API key to config.py file.
