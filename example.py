from forexrateapi.client import Client

api_key = 'REPLACE_ME'
client = Client(api_key)

result = client.fetchSymbols()
print(result)

result = client.fetchLive(base='USD', currencies=['AUD', 'CAD', 'GBP', 'JPY'])
print(result)

result = client.fetchHistorical(date='2021-04-05', base='USD', currencies=['AUD', 'CAD', 'GBP', 'JPY'])
print(result)

result = client.ohlc(base='USD', currency='EUR', date='2021-04-05', date_type=None)
print(result)

result = client.convert(from_currency='USD', to_currency='EUR', amount=100, date='2021-04-05')
print(result)

result = client.timeframe(start_date='2021-04-05', end_date='2021-04-06', base='USD', currencies=['AUD', 'CAD', 'GBP', 'JPY'])
print(result)

result = client.change(start_date='2021-04-05', end_date='2021-04-06', base='USD', currencies=['AUD', 'CAD', 'GBP', 'JPY'])
print(result)

result = client.usage()
print(result)
