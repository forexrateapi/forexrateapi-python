# ForexRateAPI

forexrateapi is the official Python API wrapper for ForexRateAPI.com. This allows you to quickly integrate our foreign exchange rate API and currency conversion API into your application. Check https://forexrateapi.com documentation for more information.

## Installation

Install the latest release with:


    pip install forexrateapi

## Usage

```python
from forexrateapi.client import Client

api_key = 'SET_YOUR_API_KEY_HERE'
client = Client(api_key)
```
---
## Documentation

#### fetchSymbols()
```python
client.fetchSymbols()
```

[Link](https://forexrateapi.com/documentation#api_symbol)

---
#### fetchLive(base, currencies)

- `base` <[string]> Optional. Pass in a base currency, defaults to USD.
- `currencies` <[List]<[string]>> Optional. Pass in an list of currencies to return values for.

```python
client.fetchLive(base='USD', currencies=['AUD', 'CAD', 'GBP', 'JPY'])
```

[Link](https://forexrateapi.com/documentation#api_realtime)

---
#### fetchHistorical(date, base, currencies)

- `date` <[string]> Required. Pass in a string with format `YYYY-MM-DD`
- `base` <[string]> Optional. Pass in a base currency, defaults to USD.
- `currencies` <[List]<[string]>> Optional. Pass in an list of currencies to return values for.

```python
client.fetchHistorical(date='2024-02-05', base='USD', currencies=['AUD', 'CAD', 'GBP', 'JPY'])
```

[Link](https://forexrateapi.com/documentation#api_historical)

---
#### convert(from_currency, to_currency, amount, date)

- `from_currency` <[string]> Optional. Pass in a base currency, defaults to USD.
- `to_currency` <[string]> Required. Specify currency you would like to convert to.
- `amount` <[number]> Required. The amount to convert.
- `date` <[string]> Optional. Specify date to use historical midpoint value for conversion with format `YYYY-MM-DD`. Otherwise, it will use live exchange rate date if value not passed in.

```python
client.convert(from_currency='USD', to_currency='EUR', amount=100, date='2024-02-05')
```

[Link](https://forexrateapi.com/documentation#api_convert)

---
#### timeframe(start_date, end_date, base, currencies)

- `start_date` <[string]> Required. Specify the start date of your timeframe using the format `YYYY-MM-DD`.
- `end_date` <[string]> Required. Specify the end date of your timeframe using the format `YYYY-MM-DD`.
- `base` <[string]> Optional. Pass in a base currency, defaults to USD.
- `currencies` <[List]<[string]>> Optional. Pass in an list of currencies to return values for.

```python
client.timeframe(start_date='2024-02-05', end_date='2024-02-06', base='USD', currencies=['AUD', 'CAD', 'GBP', 'JPY'])
```

[Link](https://forexrateapi.com/documentation#api_timeframe)

---
#### change(start_date, end_date, base, currencies)

- `start_date` <[string]> Required. Specify the start date of your timeframe using the format `YYYY-MM-DD`.
- `end_date` <[string]> Required. Specify the end date of your timeframe using the format `YYYY-MM-DD`.
- `base` <[string]> Optional. Pass in a base currency, defaults to USD.
- `currencies` <[List]<[string]>> Optional. Pass in an list of currencies to return values for.

```python
client.change(start_date='2024-02-05', end_date='2024-02-06', base='USD', currencies=['AUD', 'CAD', 'GBP', 'JPY'])
```

[Link](https://forexrateapi.com/documentation#api_change)

---
**[Official documentation](https://forexrateapi.com/documentation)**


---
## FAQ

- How do I get an API Key?

    Free API Keys are available [here](https://forexrateapi.com).

- I want more information

    Checkout our FAQs [here](https://forexrateapi.com/faq).


## Support

For support, get in touch using [this form](https://forexrateapi.com/contact).


[List]: https://www.w3schools.com/python/python_datatypes.asp 'List'
[number]: https://www.w3schools.com/python/python_datatypes.asp 'Number'
[string]: https://www.w3schools.com/python/python_datatypes.asp 'String'