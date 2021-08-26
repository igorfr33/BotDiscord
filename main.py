import requests

request = requests.get('https://api.coingecko.com/api/v3/coins/plant-vs-undead-token'.format())

pvu_data = request.json()

print('Preco de Venda em Real: {}'.format(pvu_data['market_data']['current_price']['brl']))
