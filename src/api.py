import requests

api = 'https://www.freetogame.com/api/games'

def requestApi():
    response = requests.get(api)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f'Erro na requisição: Código de status {response.status_code}'