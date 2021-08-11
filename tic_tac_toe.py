from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class text_game(App):
    def check_three_in_row(self):
        pass

    def check_board(self):
        pass

    ''' get_transition_table
        A general function that returns the transitions for a state s in the form of a list.     
    '''

    def update_state(self,  button_id):
        if(not "Player" in self.button_map[button_id].text and self.win_label.text == ""):
            index = ord(button_id) - 97
            row = index // 3
            col = index % 3

            if(self.player_turn == 1):
                self.button_map[button_id].background_color = "FF0000"
                self.button_map[button_id].text = "Player 1"
                self.board[row][col] = 1
            else:
                self.button_map[button_id].background_color = "0000FF"
                self.button_map[button_id].text = "Player 2"
                self.board[row][col] = 2

            if(self.check_board()):
                self.win_label.text = "%d is the winner of this game! Close to play again." %(self.player_turn)
                if(self.player_turn == 1):
                    self.win_label.color = "FF0000"
                else:
                    self.win_label.color = "0000FF"

            else:
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
        self.board = [[],[],[]]
        self.button_map = {}

        self.rel_layout = RelativeLayout()
        self.win_label = Label(
            text="",
            pos_hint = {'x': 1},
        )
        #add widgets to window

        self.a = Button(
            text="1",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.a)
        self.board[0].append(self.a)
        self.button_map["a"] = self.a
        self.a.bind(on_press=lambda x: self.update_state("a"))

        self.b = Button(
            text="2",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.b)
        self.board[0].append(self.b)
        self.button_map["b"] = self.b
        self.b.bind(on_press=lambda x: self.update_state("b"))

        self.c = Button(
            text="3",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.c)
        self.board[0].append(self.c)
        self.button_map["c"] = self.c
        self.c.bind(on_press=lambda x: self.update_state("c"))

        self.d = Button(
            text="4",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.d)
        self.board[1].append(self.d)
        self.button_map["d"] = self.d
        self.d.bind(on_press=lambda x: self.update_state("d"))

        self.e = Button(
            text="5",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.e)
        self.board[1].append(self.e)
        self.button_map["e"] = self.e
        self.e.bind(on_press=lambda x: self.update_state("e"))

        self.f = Button(
            text="5",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.f)
        self.board[1].append(self.f)
        self.button_map["f"] = self.f
        self.f.bind(on_press=lambda x: self.update_state("f"))

        self.g = Button(
            text="6",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.g)
        self.board[2].append(self.g)
        self.button_map["g"] = self.g
        self.g.bind(on_press=lambda x: self.update_state("g"))

        self.h = Button(
            text="7",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.h)
        self.board[2].append(self.h)
        self.button_map["h"] = self.h
        self.h.bind(on_press=lambda x: self.update_state("h"))

        self.i = Button(
            text="8",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFAF',
        )
        self.window.add_widget(self.i)
        self.board[2].append(self.i)
        self.button_map["i"] = self.i
        self.i.bind(on_press=lambda x: self.update_state("i"))

        self.window.add_widget(self.rel_layout)
        self.rel_layout.add_widget(self.win_label)

        return self.window


if __name__ == "__main__":
    text_game().run()
