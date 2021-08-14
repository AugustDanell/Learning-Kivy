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

    def main_menu(self):
        initial_welcome = Label(
            text = "Hello and welcome to the learner app",
        )


        quit_button = Button(
            text = "quit",
        )

        quit_button.bind(on_press=lambda x: self.quit())

        self.window.add_widget(initial_welcome)
        self.window.add_widget(quit_button)

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
