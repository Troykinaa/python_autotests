"""
Kolorado test api
"""
import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
def test_status_code():
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200
def test_piece_body():
    response = requests.get(url=f'{URL}/trainers', params= {'trainer_id':'3606'})
    assert response.json()['trainer_name'] == 'Саша'                                                                               