from kivy.app import App
from kivy.lang import Builder
from random import choice
from api import requestApi
from requestImg import getImg
import webbrowser

api = requestApi()

def filtringApi(type):
    result = []
    for i in api:
        if i['genre'] == type:
            result.append(i)
    return result

def getId(api):
    aleatoryGame = choice(api)
    for i in api:
        if i['id'] == aleatoryGame['id']:
            return i

class randomGameSelector(App):
    def build(self):
        return Builder.load_file('src/main.kv')

    def randomizeGame(self):
        game = getId(self.statusCheckbox())
        img = getImg(game)
        self.root.ids['textLabel'].text = game['title']
        self.root.ids['img'].source = img
        self.root.ids['plataforma'].text = f'Plataforma: {game["platform"]}'
        self.root.ids['publisher'].text = f'Empresa: {game["publisher"]}'
        self.root.ids['genero'].text = f'Empresa: {game["genre"]}'
        self.root.ids['site'].text = game['game_url']

    def open_link(self):
        webbrowser.open(self.root.ids['site'].text)
    
    def statusCheckbox(self):
        try:
            strategy = self.root.ids['strategy']
            mmorpg = self.root.ids['mmorpg']
            shooter = self.root.ids['shooter']
            checkbox = [strategy, mmorpg, shooter]
            for i in checkbox:
                if i.active:
                    return filtringApi(i.text)
                else:
                    return api
                    
        except Exception as e:
            print("Erro:", str(e))
            return api
            



randomGameSelector().run()
