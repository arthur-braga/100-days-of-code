from turtle import Screen
from cars import Car
from player import Player
from scoreboard import Scoreboard
import time

COLOR_LIST = ["red", "yellow", "green", "blue", "magenta", "cyan"]

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

car_list = []

player = Player()
for _ in range(20):
    car = Car(COLOR_LIST)
    car_list.append(car)
scoreboard = Scoreboard()
screen.onkey(player.move, "Up")
screen.listen()

level = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1/level)
    screen.update()
    for car in car_list:
        car.move()
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.reached_goal():
        level += 1
        scoreboard.level_complete(level)
        screen.update()
        time.sleep(1)
        scoreboard.set_score()
    if scoreboard.score == 10:
        game_is_on = False
        scoreboard.game_won()



screen.exitonclick()