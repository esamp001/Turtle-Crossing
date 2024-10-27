from turtle import Turtle
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.player_level = 0


    def update_score(self):
        self.goto(-150, 250)
        self.write(arg=f"Your Current Level: {self.player_level}", align="center", font=FONT)
