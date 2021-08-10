from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class text_game(App):
    def button_texts(self, state, button_id):
        index = ord(button_id)-97
        buttons = {
            1: ["You play dead.", "You stay where you are.", "You slowly walk back.", "You fight."],
            2: ["You re-enter the forrest in spite of the late hour", "You rest for the night", "No option", "No option"],
            3: ["You follow the trail", "You stay where you are", "No Option", "No Option"]
        }

        return buttons[state][index]

    def text_bank(self, state):
        label = {
            1: "You are walking in the woods and a bear immerges from the bushes, what do you do?",
            2: "The bear has stopped following you. Now you are back home but it is getting dark, what do you do?",
            3: "You see a dead dear by the road, someone or something has killed it, what do you do?"
        }

        return label[state]

    ''' get_transition_table
        A general function that returns the transitions for a state s in the form of a list.     
    '''

    def update_state(self, current_state, button_id):
        index =  ord(button_id) - 97
        game_states = {
                1 : [3,2,-1,-1],
                2 : [-1, 3],
                3 : [4, 1],
        }
        return game_states[current_state][index]

    ''' get_table_size
        Given that we are in a state s we need to know the size of that state table that is how many transitions there
        are, we need this to be able to know how many buttons to draw for a given state.
    '''

    def get_table_size(self, current_state):
        return len(self.get_transistion_table(current_state))



    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.state = 1

        self.scenario_text = Label(
                            text= self.text_bank(1),
                            font_size= 18,
                            color= '#CFFFFF'
                            )

        self.window.add_widget(self.scenario_text)
        #add widgets to window

        self.a = Button(
            text="A: " + self.button_texts(1, "a"),
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.a)
        self.a.bind(on_press=lambda x: self.update_state(1,"a"))

        self.b = Button(
            text="B: " + self.button_texts(1,"b"),
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.b)
        self.b.bind(on_press=lambda x: self.update_state(1,"b"))

        self.c = Button(
            text="C: " + self.button_texts(1,"c"),
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.c)
        self.c.bind(on_press=lambda x: self.update_state(1,"b"))

        self.d = Button(
            text="D: " + self.button_texts(1, "d"),
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.d)
        self.d.bind(on_press=lambda x: self.update_state(1,"d"))

        return self.window


if __name__ == "__main__":
    text_game().run()
