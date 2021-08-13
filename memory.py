from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random

class card:
    def __init__(self, type):
        self.type = type

        switch = {
            1 : "memory_assets/duck.png",
            2 : "memory_assets/dog.png",
            3 : "memory_assets/cat.png",
            4 : "memory_assets/horse.png",
            5 : "memory_assets/elephant.png",
        }
        try:
            self.link = switch[type]

        except KeyError:
            print(type, "is not a valid type, there is no such memory card!")

    def __str__(self):
        types = {
            1: "duck",
            2: "dog",
            3: "cat",
            4: "horse",
            5: "elephant",
        }

        return types[self.type]

    def __eq__(self, other):
        if(self.type == other.type):
            return True
        return False

class Memory(App):
    def fisher_yates(self):
        for i in range(len(self.card_list) - 1, 0, -1):
            rand = random.randint(0, i)
            self.card_list[i], self.card_list[rand] = self.card_list[rand], self.card_list[i]

    def update_score(self):
        self.info.text = "Current turn: Player One, Score: %d %d" %(self.score_list[0], self.score_list[1])


    def flip_card(self, id):
        index = id-1
        self.turn_counter += 1

    def add_button(self, id):
        b = Button(
            text=id,
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )

        self.window.add_widget(b)
        b.bind(on_press=lambda x: self.flip_card(b.text))
        self.button_list.append(b)

    def build(self):
        amount_of_cards = 5
        self.card_list = []
        self.player_turn = 1
        self.turn_counter = 0
        self.score_list = [0,0]

        for i in range(amount_of_cards):
            self.card_list.append(card(i+1))
            self.card_list.append(card(i+1))

        # Shuffling the cards around
        self.fisher_yates()

        # Fixing a grid:
        self.window = GridLayout()
        self.window.cols = 5
        self.button_list = []

        # Adding buttons:
        for i in range(2*amount_of_cards):
            self.add_button(str(i+1))

        # Fixing a label to say which turn it is:
        self.info = Label(
            text = "",
            size_hint=(8, 0.5),
        )
        self.update_score()
        self.window.add_widget(self.info)


        return self.window


if __name__ == "__main__":
    Memory().run()
