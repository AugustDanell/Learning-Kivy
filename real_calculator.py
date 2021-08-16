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
        self.div.bind(on_press= lambda x: self.divide())

        self.mult = Button(
            text="*",
        )
        self.mult.bind(on_press= lambda x: self.multiplicate())

        self.sub = Button(
            text="-",
        )
        self.sub.bind(on_press= lambda x: self.subtract())

        self.add = Button(
            text="+",
        )
        self.add.bind(on_press= lambda x: self.addition())

        self.zero = Button(
            text="0",
        )
        self.zero.bind(on_press= lambda x: self.bind_numbers_with(0))

        self.equal = Button(
            text="=",
        )
        self.equal.bind(on_press= lambda x: self.ans())
        self.button_window.add_widget(self.seven)
        self.button_window.add_widget(self.eight)
        self.button_window.add_widget(self.nine)
        self.button_window.add_widget(self.div)

        self.button_window.add_widget(self.four)
        self.button_window.add_widget(self.five)
        self.button_window.add_widget(self.six)
        self.button_window.add_widget(self.mult)

        self.button_window.add_widget(self.three)
        self.button_window.add_widget(self.two)
        self.button_window.add_widget(self.one)
        self.button_window.add_widget(self.sub)

        self.button_window.add_widget(self.zero)
        self.button_window.add_widget(self.add)
        self.button_window.add_widget(self.equal)

    def build(self):

        # Fixing a grid:
        self.window = GridLayout()
        self.window.cols = 1
        self.button_window = GridLayout()
        self.button_window.cols = 4

        self.answer = Label(
            text = "0",
            color = "FFFFFF",
            #background = "FFFFFF",
        )
        self.window.add_widget(self.answer)
        self.window.add_widget(self.button_window)
        self.fill_buttons()

        return self.window


if __name__ == "__main__":
    base().run()
