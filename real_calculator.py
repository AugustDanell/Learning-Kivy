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
    def bind_numbers_with(self, number):
        pass

    def fill_buttons(self):
        self.one = Button(
            text = "1",
        )
        self.one.bind(on_press= lambda x : self.bind_numbers_with(1))

        self.two = Button(
            text="2",
        )
        self.two.bind(on_press= lambda x : self.bind_numbers_with(2))

        self.three = Button(
            text="3",
        )
        self.three.bind(on_press= lambda x : self.bind_numbers_with(3))

        self.four = Button(
            text="4",
        )
        self.four.bind(on_press= lambda x : self.bind_numbers_with(4))

        self.five = Button(
            text="5",
        )
        self.five.bind(on_press= lambda x : self.bind_numbers_with(5))

        self.six = Button(
            text="6",
        )
        self.six.bind(on_press= lambda x : self.bind_numbers_with(6))

        self.seven = Button(
            text="7",
        )
        self.seven.bind(on_press= lambda x : self.bind_numbers_with(7))

        self.eight = Button(
            text="8",
        )
        self.eight.bind(on_press= lambda x : self.bind_numbers_with(8))

        self.nine = Button(
            text="9",
        )
        self.nine.bind(on_press= lambda x : self.bind_numbers_with(9))

        self.div = Button(
            text="/",
        )

        self.mult = Button(
            text="*",
        )

        self.sub = Button(
            text="-",
        )

        self.add = Button(
            text="+",
        )

        self.zero = Button(
            text="0",
        )

        self.equal = Button(
            text="=",
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
