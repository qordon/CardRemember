from kivy.uix.screenmanager import Screen
from configparser import ConfigParser

config = ConfigParser()
config.read("locales/ru.ini", "UTF-8")


class DescriptionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.description.text = config.get("DESCRIPTION", "description")
        self.game_process.text = config.get("GAME_PROCESS", "game_process")
        self.results.text = config.get("RESULTS", "results")

