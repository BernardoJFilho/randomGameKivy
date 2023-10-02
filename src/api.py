import requests

api = 'https://www.freetogame.com/api/games'

def requestApi():
    response = requests.get(api)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f'Erro na requisição: Código de status {response.status_code}'
    
    
{'id': 22, 'title': 'Wild Terra Online', 
    'thumbnail': 'https://www.freetogame.com/g/22/thumbnail.jpg', 
    'short_description': 'A medieval sandbox MMO designed with core players in mind. ', 
    'game_url': 'https://www.freetogame.com/open/wild-terra-online', 
    'genre': 'MMORPG', 'platform': 'PC (Windows)', 'publisher': 'Juvty Worlds Ltd.', 'developer': 'Juvty Worlds Ltd.', 
    'release_date': '2017-12-18', 'freetogame_profile_url': 'https://www.freetogame.com/wild-terra-online'}