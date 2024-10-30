from turtle import Turtle
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.player_level = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-150, 250)
        self.write(arg=f"Your Current Level: {self.player_level}", align="center", font=FONT)

    def score(self):
        self.player_level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER!", align="center", font=FONT)
