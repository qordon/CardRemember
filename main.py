from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder

from GameManager import GameManager
from MenuScreen import MenuScreen
from GameScreen import GameScreen
from EndScreen import EndScreen

Builder.load_file("markup/Elements.kv")
Builder.load_file("markup/MenuScreen.kv")
Builder.load_file("markup/GameScreen.kv")
Builder.load_file("markup/EndScreen.kv")
Window.size = (390, 630)

game_manager = GameManager()
screen_manager = ScreenManager()
screen_manager.add_widget(MenuScreen(game_manager, name='menu'))
screen_manager.add_widget(GameScreen(game_manager, name='game'))
screen_manager.add_widget(EndScreen(game_manager, name='end'))


class CardRememberApp(App):
    def build(self):
        return screen_manager


if __name__ == "__main__":
    CardRememberApp().run()

