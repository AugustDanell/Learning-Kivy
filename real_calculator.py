from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
import random
import time


class base(App):
    def check_numeric(self, candidate_number):
        try:
            int(candidate_number)
        except:
            return False

        return True

    def ans(self):
        # Take an expression and calculate it, start with multiplication and division:

        expression_list = self.expression.split(" ")    # 1. Split it into a list.
        new_list = []                                   # 2. Declare a list to be processed
        print("Expression list:", expression_list)
        for i in range(1,len(expression_list) -1, 1):   # 3. Loop through it, checking for operations and appending operands.

            # If we come across + or - we just save the previous operand and the operation, if it is the last operation done we save both operands.
            if(expression_list[i] == "+" or expression_list[i] == "-"):
                new_list.append(expression_list[i-1])
                new_list.append(expression_list[i])
                if(i == len(expression_list) - 2):
                    new_list.append(expression_list[i+1])

            # If, however, our operation is that of multiplication or division we handle it immedietly:
            elif(expression_list[i] == "*"):
                factor_one = expression_list[i-1]
                factor_two = expression_list[i+1]
                product = int(factor_one) * int(factor_two)
                if(len(new_list) == 0 or not self.check_numeric(new_list[len(new_list)-1])):
                    new_list.append(str(product))
                elif(len(new_list) > 0 and self.check_numeric(new_list[len(new_list)-1])):
                    new_list[len(new_list) -1] = str(product)

                expression_list[i+1] = str(product)     # Remember: We must also change the last operand in case we have something like 4*4*4, this should be 64.

            elif (expression_list[i] == "/"):
                factor_one = expression_list[i - 1]
                factor_two = expression_list[i + 1]
                quotient = int(factor_one) // int(factor_two)
                new_list.append(str(quotient))
                expression_list[i + 1] = str(quotient)  # Remember: We must also change the last operand in case we have something like 4*4*4, this should be 64.

        print("New List:", new_list)

        sum = int(new_list[0])
        for i in range(1, len(new_list) -1, 1):
            if(new_list[i] == "+"):
                sum += int(new_list[i+1])
            elif(new_list[i] == "-"):
                sum -= int(new_list[i+1])

        print(sum)
        self.expression = str(sum)
        self.answer.text = self.expression

    def bind_numbers_with(self, number):
        if(type(number) == int):
            if(self.expression == "0"):
                self.expression = str(number)
            else:
                self.expression += str(number)
        else:
            self.expression += number

        self.answer.text = self.expression

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
        self.div.bind(on_press= lambda x: self.bind_numbers_with(" / "))

        self.mult = Button(
            text="*",
        )
        self.mult.bind(on_press= lambda x: self.bind_numbers_with(" * "))

        self.sub = Button(
            text="-",
        )
        self.sub.bind(on_press= lambda x: self.bind_numbers_with(" - "))

        self.add = Button(
            text="+",
        )
        self.add.bind(on_press= lambda x: self.bind_numbers_with(" + "))

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
        self.expression = ""

        self.answer = Label(
            text = "0",
            color = "FFFFFF",
        )
        self.window.add_widget(self.answer)
        self.window.add_widget(self.button_window)
        self.fill_buttons()

        return self.window


if __name__ == "__main__":
    base().run()
