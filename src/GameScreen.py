from kivy.uix.screenmanager import Screen
import locales.ru as ru


class GameScreen(Screen):
    def __init__(self, game_manager, **kwargs):
        super().__init__(**kwargs)
        self.game_manager = game_manager

    def clear(self):
        self.card_image.source = "images/cards/" + self.game_manager.get_current_card()[0]
        self.right_amount.text = ru.right_amount_label + "0"

    def click(self, state):
        card, is_end = self.game_manager.get_next_card()
        self.card_image.source = "images/cards/" + card[0]

        if self.game_manager.check_answer(state):
            self.right_amount.text = ru.right_amount_label + str(self.game_manager.win_number)

        if is_end:
            self.parent.get_screen('end').fill_info()
            self.parent.current = 'end'

    def repeat_game(self):
        self.game_manager.clear()
        self.parent.get_screen('game').clear()
        self.parent.current = 'game'
