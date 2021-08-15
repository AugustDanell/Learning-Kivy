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
    def fill_buttons(self):
        self.one = Button(
            
        )

        self.two = Button(

        )

        self.three = Button(

        )

        self.four = Button(

        )

        self.five = Button(

        )

        self.six = Button(

        )

        self.seven = Button(

        )

        self.eight = Button(

        )

        self.nine = Button(

        )

        self.div = Button(

        )

        self.mult = Button(

        )

        self.sub = Button(

        )

        self.add = Button(

        )

        self.zero = Button(

        )

        self.equal = Button(

        )
        
    def build(self):

        # Fixing a grid:
        self.window = GridLayout()
        self.window.cols = 1
        self.button_window = GridLayout()
        self.button_window.cols = 4
        
        self.answer = Label(
            text = 0,
        )
        
        return self.window


if __name__ == "__main__":
    base().run()
