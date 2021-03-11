from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.storage.jsonstore import JsonStore
from GameManager import GameManager

kv = '''
<MainScreen>:
    card_image: card_image
    right_amount: right_amount
    
    orientation: 'vertical'
    GridLayout:
        rows: 3
        spacing: 0
        BoxLayout:
            size_hint: [1, 0.4]
        BoxLayout:
            orientation: 'vertical'
            size_hint: [0.5, 1]
            Image:
                size_hint: [1, 1]
                id: card_image
                source: 'PNG/2C.png'
                size: self.texture_size
            BoxLayout:
                size_hint: [1, 0.25]
                # orientation: 'vertical'
                padding: [35, 10, 35, 10]
                spacing: 10
                Button: 
                    text: "<"
                    font_size: "24"
                    on_press:
                        root.click(-1)
                Button:
                    text: "="
                    font_size: "24"
                    on_press:
                        root.click(0)
                Button:
                    text: ">"
                    font_size: "24"
                    on_press:
                        root.click(1)
                    
        BoxLayout:
            size_hint: [1, 0.4]
            Label:
                id: right_amount
                text: "Верно: 0"
                font_size: "24"
                
<EndScreen>:
    orientation: 'vertical'
    right_amount: right_amount
    
    
    BoxLayout:
        
    BoxLayout:
        size_hint: [1, 1]
        Label:
            id: right_amount
            font_size: "24"
    BoxLayout:
    
    
'''

Builder.load_string(kv)
Window.size = (390, 630)


class MainScreen(Screen):
    def __init__(self, game_manager, **kwargs):
        super().__init__(**kwargs)
        self.game_manager = game_manager

        self.card_image.source = "PNG/" + self.game_manager.get_current_card()[0]

    def click(self, state):
        card, is_end = self.game_manager.get_next_card()
        self.card_image.source = "PNG/" + card[0]
        print(card)

        if self.game_manager.check_answer(state):
            self.right_amount.text = "Верно: " + str(self.game_manager.win_number)

        if is_end:
            screen_manager.get_screen('end').ids.right_amount.text = self.right_amount.text
            self.parent.current = 'end'


class EndScreen(Screen):
    def __init__(self, game_manager, **kwargs):
        super().__init__(**kwargs)
        self.game_manager = game_manager

    def myfunction(self):
        self.right_amount.text = "Верно: " + str(game_manager.win_number)


game_manager = GameManager()
screen_manager = ScreenManager()
screen_manager.add_widget(MainScreen(game_manager, name='menu'))
screen_manager.add_widget(EndScreen(game_manager, name='end'))


class CardRememberApp(App):
    def build(self):
        return screen_manager


if __name__ == "__main__":
    CardRememberApp().run()

