from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class text_game(App):
    def text_bank(self, state):
        label = {
            1: "You are walking in the woods and a bear immerges from the bushes",
            2: "The bear has stopped following you. Now you are back home but it is getting dark, what do you do?",
            3: ""
        }
        
        button = {
            
        }
        
        return label[state], button[state]
        
    def get_transition(self, current_state, choice = -1):
        game_states = {
                1 : [3,2,-1,-1],
                2 : [-1, 3],
                3 : [4, 1],
        }
        if(not choice == -1):
            return game_states[current_state][choice-1]
        else:
            return len(game_states[current_state])


    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}


        self.window.add_widget()
        #add widgets to window

        return self.window


if __name__ == "__main__":
    text_game().run()
