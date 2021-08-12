from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class text_game(App):
    def check_three_in_row(self, x, y):
        ''' check_three_in_row()
            Takes in a tuple (x,y) and looks to see if it is a center point or not, where a center point is a center point
            in three in a row, either horisisontically, diagonally or vertically.
        '''
        
        if(self.board[x][y] == 0):
            return False
        else:
            player_square = self.board[x][y]
            if(x in [0,2] and y in [0,2]):
                return False    # Return corner points as false directly.

            elif(not x == 1 and y == 1):
                if(self.board[x][0] == player_square and self.board[x][2] == player_square):
                    return True

            elif(x == 1 and not y == 1):
                if(self.board[0][y] == player_square and self.board[2][y] == player_square):
                    return True

            else:
                if(self.board[1][0] == player_square and self.board[1][2] == player_square):
                    return True
                if(self.board[0][1] == player_square and self.board[2][1] == player_square):
                    return True
                if(self.board[0][0] == player_square and self.board[2][2] == player_square):
                    return True
                if(self.board[2][0] == player_square and self.board[0][2] == player_square):
                    return True

    def check_board(self):
        ''' check_board()
            Iterates accross the board and calls check_three_in_row for every coordinate of x and y.
        '''
        for x in range(3):
            for y in range(3):
                if(self.check_three_in_row(x, y)):
                    return True

        return False

    def update_state(self,  button_id):
        ''' update_state
            Updates the board. The board listens to buttons being clicked and if they are clicked, given that no player has
            won, the square that was clicked will become the player who is currently playing, and the turn will alternate to
            the other player, starting with red.
        '''

        if(not "Player" in self.button_map[button_id].text and self.win_label.text == ""):
            index = ord(button_id) - 97
            row = index // 3
            col = index % 3
            self.played_turns += 1

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

        # Declare a draw:
        if(self.played_turns == 9):
            self.win_label.color = "00FF00"
            self.win_label.text = "The game has come to a draw, no winners, close to play again."

    def build(self):
        self.window = GridLayout()
        self.window.cols = 3

        # Centers the button-window in a way that is good:
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # A counter for who is currently playing (player one or red, binary choice):
        self.player_turn = 1
        self.played_turns = 0

        # Mapping the current board and setting up a map for easy access to each button object:
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.button_map = {}

        # Setting a relative layout in which we will place our label announcing the winner:
        self.rel_layout = RelativeLayout()
        self.win_label = Label(
            text="",
            pos_hint = {'x': 1},
        )

        #adding buttons:
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
