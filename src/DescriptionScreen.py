from kivy.uix.screenmanager import Screen
import locales.ru as ru


class DescriptionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.description.text = ru.description
        self.game_process.text = ru.game_process
        self.results.text = ru.results

    def back(self):
        self.parent.current = 'menu'

