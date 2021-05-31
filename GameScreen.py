from kivy.uix.screenmanager import Screen

from GameManager import GameManager


class GameScreen(Screen):
    def __init__(self, game_manager, **kwargs):
        super().__init__(**kwargs)
        self.game_manager = game_manager

    def clear(self):
        self.card_image.source = "images/cards/" + self.game_manager.get_current_card()[0]
        self.right_amount.text = "Верно: 0"

    def click(self, state):
        card, is_end = self.game_manager.get_next_card()
        self.card_image.source = "images/cards/" + card[0]

        if self.game_manager.check_answer(state):
            self.right_amount.text = "Верно: " + str(self.game_manager.win_number)

        if is_end:
            self.parent.get_screen('end').fill_info()
            self.parent.current = 'end'