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



class base(App):

    def build(self):

        # Fixing a grid:
        self.window = GridLayout()

        # Setting up how many columns should be in the grid:
        self.window.cols = 1

        

        return self.window


if __name__ == "__main__":
    base().run()
