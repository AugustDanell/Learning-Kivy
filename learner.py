from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random
import time

class card:
    def __init__(self, id, forward, backward):
        self.id = id
        self.forward_text = forward
        self.backward_text = backward

class Learner(App):
    # Uses Fisher Yates Algorithm to shuffle the memory cards.
    def shuffle_flashcards(self):
        for i in range(len(self.flashcard_list) - 1, 0, -1):
            rand = random.randint(0, i)
            self.flashcard_list[i], self.flashcard_list[rand] = self.flashcard_list[rand], self.flashcard_list[i]

    # Quits the game.
    def quit(self):
        App.get_running_app().stop()

    def save_cards(self):
        pass

    def load_in_choice(self, text):
        split = text.split()
        id = int(split[0])
        index = id -1

        word_list = self.load_options[index]
        print(word_list)

        for word in word_list:
            front,back = word.split("-")
            new_card = card(id, front, back)
            self.flashcard_list.append(new_card)
        self.counter = 0
        self.window.clear_widgets()
        self.play_game()


    # Loads in cards:
    def load_cards(self):
        ''' load_cards
            Idea: We can have a big list where each item is a dictionary of type (string -> list).
            The string is the name of the flashcard deck, for instance Italian, and the list is the list of all the words.
            We make a button with that name and save it as such, also making a back button.
        '''

        self.flashcard_list = []
        self.window.clear_widgets()
        self.load_screen = GridLayout()
        self.load_screen.cols = 1

        self.window.add_widget(self.load_screen)
        self.load_options = []
        with open('flashcards/saved_flashcards') as file:
            text_lines = file.readlines()
            numeration = 1
            button_list = []

            for line in text_lines:
                split = line.split(";")
                cards = split[1:]
                for i in range(len(cards)):
                    cards[i] = cards[i].strip()

                self.load_options.append(cards)
                b = Button(
                    text = str(numeration) + " " + split[0],
                )
                self.load_screen.add_widget(b)
                b.bind(on_press=lambda x: self.load_in_choice(text = b.text))

                print(cards)
                numeration += 1
        print("YO")


    # Decreases the current card number with one if we want to go back to a previous card:
    def decrement_one(self):
        if(self.counter > 0):
            self.counter -= 1
            self.button_layout.clear_widgets()
            self.window.clear_widgets()
            self.play_game()

    # Does the same as decrement but increments instead that is move forward.
    def increment_one(self):
        if(self.counter+1 < len(self.flashcard_list)):
            self.counter += 1
            self.button_layout.clear_widgets()
            self.window.clear_widgets()
            self.play_game()

    # Flips a card so the other side shows itself.
    def flip_card(self):
        if(self.flipped):
            self.card_button.text = self.flashcard_list[self.counter].forward_text + " (Press to flip)"
            self.flipped = False
        else:
            self.flipped = True
            self.card_button.text = self.flashcard_list[self.counter].backward_text + " (Press to flip)"

    # Plays the game with the flashcards.
    def play_game(self):
        self.button_layout = GridLayout(
            size_hint_y = None,
            height = 50,
        )
        self.button_layout.cols = 3
        self.flipped = False
        self.card_button = Button(
            text = self.flashcard_list[self.counter].forward_text + " (Press to flip)",
            background_color = (0, 1, 1, 1),
            color = "000000",
        )

        self.next = Button(
            text = "Press here to continue to the next card.",
        )

        self.back = Button(
            text = "Press here to go back."
        )

        self.window.add_widget(self.card_button)
        self.card_button.bind(on_press = lambda x: self.flip_card())

        self.window.add_widget(self.button_layout)
        if(not self.counter+1 == len(self.flashcard_list)):
            self.button_layout.add_widget(self.next)
            self.next.bind(on_press=lambda x: self.increment_one())

        if(not self.counter == 0):
            self.button_layout.add_widget(self.back)
            self.back.bind(on_press=lambda x: self.decrement_one())

        self.button_layout.add_widget(self.quit_button)

    # Adds a flash card to the deck.
    def append_flashcard(self):
        new_card = card(self.flashcards-self.flashcards_left, self.front_text.text, self.back_text.text)
        self.flashcard_list.append(new_card)
        self.create_flashcard()

    # Creates a flashcard.
    def create_flashcard(self):
        self.window.clear_widgets()
        if(self.flashcards_left == 0):
            self.card_counter = 0
            self.shuffle_flashcards()
            self.play_game()
        else:
            print("yo")
            self.flashcards_left -= 1 #  Exhausting one flash card.
            self.label.text = "Enter the associated texts below, what you want in the front of the card, and what you want in the back."
            self.window.add_widget(self.label)
            self.front_text = TextInput(
                multiline = True,
                text = "Front side."
            )

            self.back_text = TextInput(
                multiline = True,
                text="Back side."
            )

            self.window.add_widget(self.front_text)
            self.window.add_widget(self.back_text)

            self.add_card = Button(
                text = "Add card",
            )

            self.add_card.bind(on_press= lambda x: self.append_flashcard())
            self.window.add_widget(self.add_card)

    # Takes information from a text field.
    def extract_from_text_field(self):
        try:
            self.flashcards = int(self.text_form.text)
            self.window.clear_widgets()
            if(self.flashcards <= 0):
                raise Exception
            else:
                self.flashcard_list = []
                self.flashcards_left = self.flashcards
                self.create_flashcard()
        except:
            self.flashcards = 0
            self.window.clear_widgets()
            self.label.text = "Please, enter in a valid integer greater than zero, how many flashcards do you want?"
            self.handle_integer_input()

    # Takes integer input making up the size of the deck.
    def handle_integer_input(self):
        self.window.add_widget(self.label)

        self.text_form = TextInput(
            multiline=False,
        )

        self.window.add_widget(self.text_form)

        self.proceed = Button(
            text="Proceed",
        )

        self.window.add_widget(self.proceed)
        self.flashcards = 0
        self.proceed.bind(on_press= lambda x: self.extract_from_text_field())

    # Creates a view where the player can decide how many cards to have.
    def set_cards(self):
        self.window.clear_widgets() # Clears widgets from the previous view.
        self.counter = 0            # Initiate a counter that alternates back and forth so we can write on the back of the card.

        self.label = Label(
            text = "How many flashcards do you want to make (enter in a number and the proceed button)?",
        )

        self.handle_integer_input()

    def build(self):
        # State
        self.state = "menu"

        # Fixing a grid:
        self.window = GridLayout()
        self.window.cols = 1

        # Main program loop:
        self.main_menu() # Into View 1

        return self.window

    # View 1, the main menu.
    def main_menu(self):
        initial_welcome = Label(
            text = "Hello and welcome to the learner app",
        )

        self.start = Button(
            text = "Set Flashcards",
        )

        self.load = Button(
            text = "Load Flashcards",
        )

        self.quit_button = Button(
            text = "Quit",
        )

        self.load.bind(on_press=lambda x: self.load_cards())
        self.quit_button.bind(on_press=lambda x: self.quit())
        self.start.bind(on_press=lambda x: self.set_cards())

        self.window.add_widget(self.start)
        self.window.add_widget(self.load)
        self.window.add_widget(self.quit_button)

if __name__ == "__main__":
    Learner().run()
