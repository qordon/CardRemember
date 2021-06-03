from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout


class ChoiceBanner(BoxLayout):
    pass


class EndScreen(Screen):
    def __init__(self, game_manager, **kwargs):
        super().__init__(**kwargs)
        self.game_manager = game_manager
        self.right_expected_choices = 0

    def fill_info(self):
        self.clear()
        self.fill_banner_results()
        self.fill_statistics()

    def fill_banner_results(self):
        grid = self.ids["results"]
        for i in range(len(self.game_manager.answers)):
            banner = ChoiceBanner()
            banner.number_of_card.text = str(i + 1)
            banner.card_image.source = "images/cards/" + self.game_manager.cards[i][0]
            self.fill_choice(banner.expected_choice, self.game_manager.expected_answers[i])

            if self.game_manager.answers[i] == self.game_manager.expected_answers[i]:
                self.fill_choice(banner.choice, self.game_manager.answers[i])
                self.right_expected_choices += 1
            else:
                self.fill_choice_wrong(banner.choice, self.game_manager.answers[i])

            banner.probability.text = str(max(self.game_manager.probabilities[i]))
            grid.add_widget(banner)

        # last card without any choices
        banner = ChoiceBanner()
        banner.number_of_card.text = "36"
        banner.card_image.source = "images/cards/" + self.game_manager.cards[35][0]
        grid.add_widget(banner)

    def fill_choice(self, image, choice):
        if choice == 1:
            image.source = "images/icons/" + "up-arrow.png"
        if choice == 0:
            image.source = "images/icons/" + "equal.png"
        if choice == -1:
            image.source = "images/icons/" + "down-arrow.png"

    def fill_choice_wrong(self, image, choice):
        if choice == 1:
            image.source = "images/icons/" + "red-up-arrow.png"
        if choice == 0:
            image.source = "images/icons/" + "red-equal.png"
        if choice == -1:
            image.source = "images/icons/" + "red-down-arrow.png"

    def fill_statistics(self):
        self.right_percent.text = str(round(self.game_manager.win_number / 36 * 100, 2)) + " %"
        self.right_expected_choices_percent.text = str(round(self.right_expected_choices / 36 * 100, 2)) + " %"

    def repeat_game(self):
        self.game_manager.clear()
        self.parent.get_screen('game').clear()
        self.parent.current = 'game'

    def clear(self):
        self.ids["results"].clear_widgets()
        self.right_expected_choices = 0
