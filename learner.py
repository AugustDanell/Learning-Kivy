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
    def quit(self):
        App.get_running_app().stop()

    def load_cards(self):
        pass

    def play_game(self):
        pass

    def append_flashcard(self):
        new_card = card(self.flashcards-self.flashcards_left, self.front_text.text, self.back_text.text)
        self.flashcard_list.append(new_card)
        self.create_flashcard()

    def create_flashcard(self):
        self.window.clear_widgets()
        if(self.flashcards_left == 0):
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

    def set_cards(self):
        self.window.clear_widgets() # Clears widgets from the previous view.
        self.counter = 0            # Initiate a counter that alternates back and forth so we can write on the back of the card.

        self.label = Label(
            text = "How many flashcards do you want to make (enter in a number and the proceed button)?",
        )

        self.handle_integer_input()

    def main_menu(self):
        initial_welcome = Label(
            text = "Hello and welcome to the learner app",
        )

        self.start = Button(
            text = "Set Flashcards",
        )

        self.load = Button(
            text = "Load Flashcards (not in use yet)",
        )

        self.quit_button = Button(
            text = "Quit",
        )

        self.load.bind(on_press=lambda x: self.load_cards())
        self.quit_button.bind(on_press=lambda x: self.quit())
        self.start.bind(on_press=lambda x: self.set_cards())

        self.window.add_widget(initial_welcome)
        self.window.add_widget(self.start)
        self.window.add_widget(self.load)
        self.window.add_widget(self.quit_button)

    def build(self):
        # State
        self.state = "menu"

        # Fixing a grid:
        self.window = GridLayout()
        self.window.cols = 1

        # Main program loop:
        self.main_menu()

        return self.window


if __name__ == "__main__":
    Learner().run()
