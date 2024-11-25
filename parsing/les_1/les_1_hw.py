import requests
import json

# Конечная точка API
url = 'https://api.foursquare.com/v3/places/search'

# Определение параметров для запроса API
category = input(f'Введите категорию (например, кофейни, музеи, парки и т.д.): ')
city = input(f'Введите название города: ')

params = {
  	'query': category,
  	'near': city,
  	# 'open_now': 'true',
  	'sort':'RATING'
}

headers = {
    'Accept': 'application/json',
    'Authorization': 'API'
}

response = requests.request('GET', url, params=params, headers=headers)

if response.status_code == 200:
	print('Успешный запрос API!')

	data = json.loads(response.text)
	venues = data['results']

	with open('result.txt', 'w', encoding='utf-8') as f:
		for venue in venues:
			print('Название:', venue['name'], file=f)
			print('Адрес:', venue['location']['formatted_address'], file=f)
			print('\n', file=f)

else:
	print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
	print(response.text)