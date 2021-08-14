from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
import random
import time

class card:
    def __init__(self, type):
        pass



class Learner(App):
    def quit(self):
        App.get_running_app().stop()

    def load_cards(self):
        pass

    def set_cards(self):
        pass

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
