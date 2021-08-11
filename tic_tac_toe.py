from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class text_game(App):
    def button_texts(self, button_id):
        index = ord(button_id)-97
        buttons = {
           -1: ["No Option", "No Option", "No Option", "No Option"],
            1: ["You play dead.", "You slowly walk back.", "You stay where you are.", "You fight."],
            2: ["You re-enter the forrest in spite of the late hour", "You rest for the night", "No option", "No option"],
            3: ["You follow the trail", "You stay where you are", "No Option", "No Option"],
            4: ["No Option", "No Option", "No Option", "No Option"]
        }

        return buttons[self.state][index]

    def text_bank(self):
        label = {
            -1: "You wake up at the hospital in pain. The bear went to work on your body but the real source\n of your pain, you realize, is that you never got to taste those Swedish blueberries. You lose!",
            1: "You are walking in the woods and a bear immerges from the bushes, what do you do?",
            2: "The bear has stopped following you. Now you are back home but it is getting dark, what do you do?",
            3: "You see a dead dear by the road, someone ... or something has killed it, what do you do?",
            4: "You emerge from thorny shrubbery and behold the most tasty of blueberries! \nThere is no bear in sight! You have won a most tasty victory!"
        }

        return label[self.state]

    def check_three_in_row(self):
        pass

    ''' get_transition_table
        A general function that returns the transitions for a state s in the form of a list.     
    '''

    def update_state(self,  button_id):
        if(self.player_turn == 1):
            self.button_map[button_id].background_color = "FF0000"
        else:
            self.button_map[button_id].background_color = "0000FF"

        self.player_turn = (self.player_turn % 2) +1


    ''' get_table_size
        Given that we are in a state s we need to know the size of that state table that is how many transitions there
        are, we need this to be able to know how many buttons to draw for a given state.
    '''

    def get_table_size(self, current_state):
        return len(self.get_transistion_table(current_state))



    def build(self):
        self.window = GridLayout()
        self.window.cols = 3
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.player_turn = 1
        self.button_map = {}
        #add widgets to window

        self.a = Button(
            text="1",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.a)
        self.button_map["a"] = self.a
        self.a.bind(on_press=lambda x: self.update_state("a"))

        self.b = Button(
            text="2",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.b)
        self.button_map["b"] = self.b
        self.b.bind(on_press=lambda x: self.update_state("b"))

        self.c = Button(
            text="3",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.c)
        self.button_map["c"] = self.c
        self.c.bind(on_press=lambda x: self.update_state("c"))

        self.d = Button(
            text="4",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.d)
        self.button_map["d"] = self.d
        self.d.bind(on_press=lambda x: self.update_state("d"))

        self.e = Button(
            text="5",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.e)
        self.button_map["e"] = self.e
        self.e.bind(on_press=lambda x: self.update_state("e"))

        self.f = Button(
            text="5",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.f)
        self.button_map["f"] = self.f
        self.f.bind(on_press=lambda x: self.update_state("f"))

        self.g = Button(
            text="6",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.g)
        self.button_map["g"] = self.g
        self.g.bind(on_press=lambda x: self.update_state("g"))

        self.h = Button(
            text="7",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.h)
        self.button_map["h"] = self.h
        self.h.bind(on_press=lambda x: self.update_state("h"))

        self.i = Button(
            text="8",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.i)
        self.button_map["i"] = self.i
        self.i.bind(on_press=lambda x: self.update_state("i"))

        return self.window


if __name__ == "__main__":
    text_game().run()
