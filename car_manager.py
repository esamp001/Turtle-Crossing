import turtle
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_DISTANCE = 5 #Speed of car
MOVING_INCREMENT = 0.9 #Increment the speed of car every level

class CarManager:
    def __init__(self):
        self.level = 0.1
        self.cars = []  # saved all turtles in car variable when append

    def create_multiple_cars(self, num_cars):
        for _ in range(num_cars): #get the index and stop to 1
            new_car = Turtle(shape="square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()

            # STARTING X AXIS OF CAR
            y = random.randint(-250, 300)
            x = random.randint(-200, 500)
            new_car.goto(x, y)

            new_car.setheading(180)
            self.cars.append(new_car) #append it to car emptry string

    def move_forward(self):
        for moving in self.cars:
            moving.forward(10)
            if moving.xcor() < - 400:
                moving.setx(400)

    def increase_level(self):
        self.level *= MOVING_INCREMENT







