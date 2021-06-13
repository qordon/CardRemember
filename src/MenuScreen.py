from kivy.uix.screenmanager import Screen
import locales.ru as ru


class MenuScreen(Screen):
    def __init__(self, game_manager, **kwargs):
        super().__init__(**kwargs)
        self.game_manager = game_manager
        self.start_label.text = ru.start_label
        self.rules_label.text = ru.rules_label

    def start(self):
        self.game_manager.clear()
        self.parent.get_screen('game').clear()
        self.parent.current = 'game'

    def go_to_description_page(self):
        self.parent.current = 'description'
