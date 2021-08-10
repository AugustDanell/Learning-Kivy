from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class text_game(App):
    def text_bank(self):
        label = {
            1: "Operation is set to addition!",
            2: "Operation is set to subtraction!",
            3: "Operation is set to multiplication!",
            4: "Operation is set to division!"
        }

        return label[self.state]

    def update(self):
        self.scenario_text.text = self.text_bank()

    ''' get_transition_table
        A general function that returns the transitions for a state s in the form of a list.     
    '''

    def update_state(self,  button_id):
        index =  ord(button_id) - 97
        game_states = {
                1 : [1,2,3,4],
                2 : [1,2,3,4],
                3 : [1,2,3,4],
                4 : [1,2,3,4],
        }
        self.state = game_states[self.state][index]
        self.update()

    ''' get_table_size
        Given that we are in a state s we need to know the size of that state table that is how many transitions there
        are, we need this to be able to know how many buttons to draw for a given state.
    '''

    def get_table_size(self, current_state):
        return len(self.get_transistion_table(current_state))

    def calculate(self):
        try:
            a = int(self.variable_one.text)
            b = int(self.variable_two.text)
            operations = {
                1: a + b,
                2: a - b,
                3: a * b,
                4: a / b,
            }

            self.scenario_text.text = "Answer is: " + str(operations[self.state])
        except ZeroDivisionError:
            self.scenario_text.text = "Please make no divisions with zero! Try again!"
        except ValueError:
            if(self.variable_two.text == ""):
                self.scenario_text.text = "Please let b be a real value!"
            elif(self.variable_one.text == ""):
                self.scenario_text.text = "Set a value for numerator a!"
            else:
                self.scenario_text.text = "Please only use numeric values"


    def build(self):
        self.window = GridLayout()
        self.button_box = BoxLayout()
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

        # Adding buttons:
        self.a = Button(
            text="Set Addition",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.a)
        self.a.bind(on_press=lambda x: self.update_state("a"))

        self.b = Button(
            text="Set Subtraction",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.b)
        self.b.bind(on_press=lambda x: self.update_state("b"))

        self.c = Button(
            text="Set Multiplication",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.c)
        self.c.bind(on_press=lambda x: self.update_state("c"))

        self.d = Button(
            text="Set Division",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.d)
        self.d.bind(on_press=lambda x: self.update_state("d"))

        self.variable_one = TextInput(
                    multiline= False,
                    padding_y= (12,20),
                    size_hint= (1, 0.5)
                    )

        self.variable_two = TextInput(
                    multiline= False,
                    padding_y= (12,20),
                    size_hint= (1, 0.5)
                    )

        self.window.add_widget(self.variable_one)
        self.window.add_widget(self.variable_two)

        self.calculate_button = Button(
            text="Calculate",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )

        self.calculate_button.bind(on_press=lambda x: self.calculate())
        self.window.add_widget(self.calculate_button)

        return self.window


if __name__ == "__main__":
    text_game().run()
