from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from api import requestApi
from requestImg import getImg
from random import choice
import webbrowser

api = requestApi()

def filtringApi(type):
    result = []
    print(type)
    for j in type:
        for i in api:
            if i['genre'] == j:
                result.append(i)
    return result

def getId(api):
    aleatoryGame = choice(api)
    for i in api:
        if i['id'] == aleatoryGame['id']:
            return i
        

class randomGameSelector(App):
    def build(self):
        Config.set('graphics', 'width', '400')
        Config.set('graphics', 'height', '600')
        return Builder.load_file('src/main.kv')

    def randomizeGame(self):
        game = getId(self.statusCheckbox())
        img = getImg(game)
        self.root.ids['textLabel'].text = game['title']
        self.root.ids['img'].source = img
        self.root.ids['plataforma'].text = f'Plataforma: {game["platform"]}'
        self.root.ids['publisher'].text = f'Empresa: {game["publisher"]}'
        self.root.ids['genero'].text = f'Empresa: {game["genre"]}'
        self.root.ids['release_date'].text = f'Data de lançamento: {game["release_date"]}'
        self.root.ids['site'].text = game['game_url']

    def open_link(self):
        webbrowser.open(self.root.ids['site'].text)
    
    def statusCheckbox(self):
        strategy = self.root.ids['strategy']
        mmorpg = self.root.ids['mmorpg']
        shooter = self.root.ids['shooter']
        checkbox = [strategy, mmorpg, shooter]
        arrayText = []
        for i in checkbox:
            if i.active:
                arrayText.append(i.text)
            elif len(arrayText) == 0:
                return api
        return filtringApi(arrayText)
            



randomGameSelector().run()
