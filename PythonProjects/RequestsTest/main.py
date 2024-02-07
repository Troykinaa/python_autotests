"""
Kolorado test api
"""
import requests
URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json','trainer_token': 'bef656c5bf27710156cd87587059aa4f'}

#body = {
#    "name": "Mars",
#    "photo": "https://dolnikov.ru/pokemons/albums/007.png"
#}

#response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
#print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

#body = {
#    "pokemon_id": "28999",
#    "name": "Luna"
#}

#response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
#print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

#body = {
#    "pokemon_id": "28999"
#}

#response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=5)
#print(f'Статус код: {response.status_code}. Сообщение: {response.text}')