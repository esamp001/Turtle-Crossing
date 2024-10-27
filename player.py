from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle") #Create shape of turtle
        self.left(90) #Turn the turtle to 90degree angle
        self.penup() #Penup
        self.goto(STARTING_POSITION) #then go to starting position

    def move_up(self):
        y = self.ycor()
        self.sety(y + MOVE_DISTANCE)

    def move_down(self):
        y = self.ycor()
        self.sety(y - MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)