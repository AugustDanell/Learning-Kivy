from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
import random
import time

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

    def un_flip(self, id):
        index = id-1

        # Unflipping the card:
        self.display_list[index].clear_widgets()
        self.add_button(str(id))

    def flip_card(self, id):
        # Setting the index and checking if it is a won card already, and if so, we should do nothing:
        index = id - 1
        if(index in self.winning_indices):
            return 0

        # Incrementing the turn counter:
        self.turn_counter += 1


        # Count flips, set as flipped and potentially alternate turn:
        if(self.turn_counter == 3):
            self.turn_counter = 0
            first_card, second_card = self.flipped_cards

            # See if we got two of the same:
            is_pair = False
            print(first_card, second_card)
            if(self.card_list[first_card] == self.card_list[second_card]):
                print("Ok, they are the same")
                is_pair = True
                self.winning_indices.append(first_card)
                self.winning_indices.append(second_card)

            if(not is_pair):
                print("Unflipping")
                self.un_flip(first_card+1)
                self.un_flip(second_card+1)
                self.player_turn = (self.player_turn % 2) + 1
                self.flipped_cards = [0,0]

            return 0

        # Flipping the card:
        self.display_list[index].clear_widgets()
        memory_photo = Image(source= self.card_list[index].link)
        self.display_list[index].add_widget(memory_photo)
        self.flipped_cards[self.turn_counter-1] = id-1

    def add_button(self, id):
        b = Button(
            text=id,
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )

        self.display_list[int(id)-1].add_widget(b)
        b.bind(on_press=lambda x: self.flip_card(int(b.text)))
        self.button_list.append(b)

    def fill_buttons(self):
        for id in range (1,(self.amount_of_cards*2)+1):
            self.add_button(str(id))

    def fill_sub_layouts(self):
        for layout in self.display_list:
            self.window.add_widget(layout)

    def build(self):
        self.amount_of_cards = 5
        self.flipped_cards = [0,0] # Holds the index of the two flipped cards.
        self.display_list = [GridLayout(cols = 1) for i in range(self.amount_of_cards*2)]
        self.winning_indices = []

        self.card_list = []
        self.player_turn = 1
        self.turn_counter = 0
        self.score_list = [0,0]

        for i in range(self.amount_of_cards):
            self.card_list.append(card(i+1))
            self.card_list.append(card(i+1))

        # Shuffling the cards around
        self.fisher_yates()

        # Fixing a grid:
        self.window = GridLayout()
        self.window.cols = 5
        self.button_list = []

        # Generating subgrids in the window layout:
        self.fill_sub_layouts()

        # Adding buttons:
        self.fill_buttons()

        # Fixing a label to say which turn it is:
        self.info = Label(
            text = "",
            size_hint=(8, 0.5),
        )
        self.update_score()
        #self.window.add_widget(self.info)


        return self.window


if __name__ == "__main__":
    Memory().run()
