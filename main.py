from tkinter import *
from PIL import Image, ImageTk
import os
import random
from GameManager import GameManager


class Window(Tk):
    def __init__(self, game_manager=None):
        super().__init__()
        self.game_manager = game_manager
        game_manager.shuffle_deck()

        self.title("CardRemember")
        self.geometry('720x480+400+100')
        self.resizable(width=False, height=False)

        img = Image.open("PNG/" + self.game_manager.get_current_card()[0])
        img = img.resize((200, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.panel_img = Label(self, image=img)
        self.panel_img.image = img
        self.panel_img.place(relx=.4, rely=.48, anchor="c", height=500, width=500, bordermode=OUTSIDE)

        card_name, _ = game_manager.get_current_card()
        self.card_name_lbl = Label(text=card_name,
                          font="Arial 24")
        self.card_name_lbl.place(relx=.4, rely=.48, anchor="c", height=50, width=200, bordermode=OUTSIDE)

        self.btn_card_greater = Button(self,
                                 text="↑",
                                 font=("", 28),
                                 command=lambda: self.button_clicked(1))
        self.btn_card_greater.place(relx=.7, rely=.36, anchor="c", width=120, height=50, bordermode=OUTSIDE)

        self.btn_card_equal = Button(self,
                                    text="=",
                                    font=("", 30),
                                    command=lambda: self.button_clicked(0))
        self.btn_card_equal.place(relx=.7, rely=.48, anchor="c", width=120, height=50, bordermode=OUTSIDE)

        self.btn_card_less = Button(self,
                                    text="↓",
                                    font=("", 28),
                                    command=lambda: self.button_clicked(-1))
        self.btn_card_less.place(relx=.7, rely=.6, anchor="c", width=120, height=50, bordermode=OUTSIDE)

        self.win_lbl = Label(text="Правильно угаданных: 0",
                             font="Arial 16")
        self.win_lbl.place(relx=.3, rely=.2, anchor="c", width=260, height=50, bordermode=OUTSIDE)

    def insert_card_image(self, filepath):
        img = Image.open(filepath)
        img = img.resize((200, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.panel_img.image = img

    def button_clicked(self, state):
        card_name, card_number = self.game_manager.get_next_card()
        self.card_name_lbl['text'] = card_name
        self.insert_card_image(filepath="PNG/" + str(card_name))


        print("Iterator: " + str(self.game_manager.iterator))
        if self.game_manager.check_answer(state):
            self.win_lbl['text'] = "Правильно угаданных: " + str(self.game_manager.win_number)

        print(self.game_manager.win_number)





gM = GameManager()
root = Window(gM)
# gM.shuffle_deck()
# print(gM.cards)
root.mainloop()

