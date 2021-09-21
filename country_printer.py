from turtle import Turtle

class CountryPrinter(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def write_country(self, x_cor, y_cor, state):
        self.goto(x=x_cor, y=y_cor)
        self.write(state, font=("Arial", 10))