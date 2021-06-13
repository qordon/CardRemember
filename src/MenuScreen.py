from kivy.uix.screenmanager import Screen


class MenuScreen(Screen):
    def __init__(self, game_manager, **kwargs):
        super().__init__(**kwargs)
        self.game_manager = game_manager

    def start(self):
        self.game_manager.clear()
        self.parent.get_screen('game').clear()
        self.parent.current = 'game'

    def go_to_description_page(self):
        self.parent.current = 'description'
