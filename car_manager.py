import turtle
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_DISTANCE = 5 #Speed of car
MOVING_INCREMENT = 10 #Increment the speed of car every level



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []  # saved all turtles in car variable when append
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.penup()

        # STARTING X AXIS OF CAR
        y = random.randint(-250, 250)
        x = random.randint(-200, 500)
        self.goto(x, y)
        self.setheading(180)

    def move_forward(self):
        self.forward(10)
        if self.xcor() < - 400:
            self.setx(400)

    def start_moving(self):
        self.move_forward()
        turtle.Screen().ontimer(self.start_moving, 100)

    def create_multiple_cars(self, num_cars):
        for _ in range(min(num_cars, 10)): #get the index and stop to 1
                new_car = CarManager() #call the car attributes from car class
                new_car.start_moving()
                self.cars.append(new_car) #append it to car emptry string
    #
    # def moving_cars(self):
    #     x = self.xcor()







