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
screen.onkeypress(player.move_up, "Up") #Make turtle go up
screen.onkeypress(player.move_down, "Down") #Make turtle go down

car_manager = CarManager()
car_manager.create_multiple_cars(20)
score = Scoreboard()
score.update_score()

game_is_on = True
while game_is_on:
    time.sleep(car_manager.level)
    screen.update() #Update screen
    car_manager.move_forward()

    for car in car_manager.cars:
        if player.distance(car) < 20: #Collision to player and car
            game_is_on = False
            score.game_over()

    if player.ycor() > 280:
        player.reset_position()
        score.score()
        car_manager.increase_level()

screen.exitonclick()
