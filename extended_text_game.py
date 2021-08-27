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
            1: ["You try to rationally navigate yourself home, walking on the street", "You ask a stranger for help.", "No option", "No option"],
            2: ["You try to rationally navigate yourself home, walking on the street", "No option", "No option", "No option"],
            3: ["You walk away, intent on coming back later.", "You approach the officers to have a talk.", "You attempt to sneak into your room.", "No Option"],
            4: ["You climb the gutter.", "You climb the ladder to the roof.", "No option.", "No option."],
            5: [],
            6: [],
            7: [],
            8: [],
        }

        return buttons[self.state][index]

    def text_bank(self):
        label = {
           -1: "The gutter dislodges and you fall to your death.",
            1: "You wake up stripped of all pocessions but for your clothes and keys home.",
            2: "The stranger you ask for help smell narcotics on you and decides to ignore you.\nWhat do you do?",
            3: "Next to your appartment complex there is a group of police officers. What do you do?",
            4: "You know there is a roof entrance. Either you could climb the gutter or you could take\nthe ladder, what do you do?",
            5: "They arrest you on the spot, matching your ID with the adress.",
            6: "You return and the police officers are gone.",
            7: "You find yourself in jail and you have to get home."
        }

        return label[self.state]

    def update(self):
        self.a.text = self.button_texts("a")
        self.b.text = self.button_texts("b")
        self.c.text = self.button_texts("c")
        self.d.text = self.button_texts("d")

        if(self.state == -1):
            self.scenario_text.color = "FF0000"
        elif (self.state == 4):
            self.scenario_text.color = "0000FF"

        self.scenario_text.text = self.text_bank()

    ''' get_transition_table
        A general function that returns the transitions for a state s in the form of a list.     
    '''

    def update_state(self,  button_id):
        index =  ord(button_id) - 97
        game_states = {
                1 : [3,2,-1,-1],
                2 : [-1, 3],
                3 : [4, 1],
        }
        print(index)
        self.state = game_states[self.state][index]
        self.update()

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
                            text= self.text_bank(),
                            font_size= 18,
                            color= '#CFFFFF'
                            )

        self.window.add_widget(self.scenario_text)
        #add widgets to window

        self.a = Button(
            text="A: " + self.button_texts("a"),
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.a)
        self.a.bind(on_press=lambda x: self.update_state("a"))

        self.b = Button(
            text="B: " + self.button_texts("b"),
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.b)
        self.b.bind(on_press=lambda x: self.update_state("b"))

        self.c = Button(
            text="C: " + self.button_texts("c"),
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.c)
        self.c.bind(on_press=lambda x: self.update_state("c"))

        self.d = Button(
            text="D: " + self.button_texts("d"),
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.d)
        self.d.bind(on_press=lambda x: self.update_state("d"))

        return self.window


if __name__ == "__main__":
    text_game().run()
