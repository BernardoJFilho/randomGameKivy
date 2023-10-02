from kivy.app import App
from kivy.lang import Builder
from random import choice
from api import requestApi
from requestImg import getImg
import webbrowser
import time

api = requestApi()

KV = '''
BoxLayout:
    orientation: 'vertical'

    BoxLayout:
        orientation: 'horizontal'
        # spacing: 5
        
        CheckBox:
            id: strategy_checkbox
            padding: [0, 0]
        Label:
            text: 'Strategy'
            size_hint_x: None

        CheckBox:
            id: mmorpg_checkbox
            padding: [0, 0]
        Label:
            text: 'MMORPG'
            size_hint_x: None

        CheckBox:
            id: shooter_checkbox
            padding: [0, 0]
        Label:
            text: 'Shooter'
            size_hint_x: None
    
    Label:
        id: textLabel
        text: 'Escolha suas preferências:'
        font_size: 20

    Image:
        id: img
        source: 'src/images/images.jpg'
        size_hint: None, None
        size: 200, 200
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
    Label:
        id: plataforma
        text: ''
    
    Button:
        id: site
        text: ''
        background_normal: ''
        background_color: 0, 0, 0, 0  # Define o botão sem aparência de botão
        color: 0, 0, 1, 1  # Cor do texto (azul)
        on_release: app.open_link()

    Button:
        id: button
        on_press: app.randomizeGame()
        text: 'Start'
        size_hint: None, None
        size: 150, 50
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}


'''

def getId(api):
    aleatoryGame = choice(api)
    for i in api:
        if i['id'] == aleatoryGame['id']:
            return i

class AppGame(App):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.root.ids['textLabel'].text = 'Qual jogo voce quer jogar hoje?'
        # self.root.ids['Strategy'].text = 'Strategy'
        # MMORPG_checkbox = CheckBox(id='MMORPG', text='MMORPG')
        # shooter_checkbox = CheckBox(id='shooter', text='Shooter')


    def randomizeGame(self):
        game = getId(api)
        img = getImg(game)
        time.sleep(2.5)
        self.root.ids['textLabel'].text = game['title']
        self.root.ids['plataforma'].text = game['platform']
        self.root.ids['site'].text = game['game_url']
        self.root.ids['img'].source = img
        
    def open_link(self):
        webbrowser.open(self.root.ids['site'].text)

        

AppGame().run()
