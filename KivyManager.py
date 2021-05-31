from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.storage.jsonstore import JsonStore

from GameManager import GameManager

Builder.load_file("markup/Elements.kv")
Builder.load_file("markup/MenuScreen.kv")
Builder.load_file("markup/GameScreen.kv")
Builder.load_file("markup/EndScreen.kv")
Window.size = (390, 630)


class MenuScreen(Screen):
    def __init__(self, game_manager, **kwargs):
        super().__init__(**kwargs)
        self.game_manager = game_manager

    def start(self):
        self.game_manager.clear()
        screen_manager.get_screen('game').clear()
        self.parent.current = 'game'


class GameScreen(Screen):
    def __init__(self, game_manager, **kwargs):
        super().__init__(**kwargs)
        self.game_manager = game_manager

        self.card_image.source = "PNG/" + self.game_manager.get_current_card()[0]

    def clear(self):
        self.card_image.source = "PNG/" + self.game_manager.get_current_card()[0]
        self.right_amount.text = "Верно: 0"

    def click(self, state):
        card, is_end = self.game_manager.get_next_card()
        self.card_image.source = "PNG/" + card[0]
        print(card)

        if self.game_manager.check_answer(state):
            self.right_amount.text = "Верно: " + str(self.game_manager.win_number)

        if is_end:
            screen_manager.get_screen('end').fill_info()
            self.parent.current = 'end'


class EndScreen(Screen):
    def __init__(self, game_manager, **kwargs):
        super().__init__(**kwargs)
        self.game_manager = game_manager
        self.right_expected_choices = 0

    def fill_banner_results(self):
        grid = self.ids["results"]
        for i in range(len(self.game_manager.answers)):
            banner = ChoiceBanner()
            banner.number_of_card.text = str(i + 1)
            banner.card_image.source = "PNG/" + self.game_manager.cards[i][0]
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
        banner.card_image.source = "PNG/" + self.game_manager.cards[35][0]
        grid.add_widget(banner)

    def fill_choice(self, image, choice):
        if choice == 1:
            image.source = "PNG/" + "up-arrow.png"
        if choice == 0:
            image.source = "PNG/" + "equal.png"
        if choice == -1:
            image.source = "PNG/" + "down-arrow.png"

    def fill_choice_wrong(self, image, choice):
        if choice == 1:
            image.source = "PNG/" + "red-up-arrow.png"
        if choice == 0:
            image.source = "PNG/" + "red-equal.png"
        if choice == -1:
            image.source = "PNG/" + "red-down-arrow.png"

    def fill_info(self):
        self.clear()
        self.right_percent.text = str(round(game_manager.win_number/36*100, 2)) + " %"
        self.fill_banner_results()
        self.right_expected_choices_percent.text = str(round(self.right_expected_choices / 36 * 100, 2)) + " %"
        print(self.game_manager.cards)

    def repeat_game(self):
        self.game_manager.clear()
        screen_manager.get_screen('game').clear()
        self.parent.current = 'game'

    def clear(self):
        self.ids["results"].clear_widgets()
        self.right_expected_choices = 0


class ChoiceBanner(BoxLayout):
    pass


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

