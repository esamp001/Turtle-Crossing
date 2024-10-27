import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.tracer(0) #No delay on screen
screen.listen()

player = Player() #Call turtle (Player)
screen.onkeypress(player.move_up, "w") #Make turtle go up
screen.onkeypress(player.move_down, "s") #Make turtle go down

car_manager = CarManager()
car_manager.create_multiple_cars(40)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update() #Update screen
    car_manager.move_forward()

    if player.ycor() > 280:
        player.reset_position()