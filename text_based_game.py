from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class text_game(App):
    def get_transition(self, current_state, choice):
        game_states = {
                1 : [3,2,-1,-1],
                2 : [-1, 3],
                3 : [],
        }

        return game_states[current_state][choice-1]

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        #add widgets to window

        return self.window


if __name__ == "__main__":
    text_game().run()
