import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


my_player=Player()
my_Car=CarManager()
my_Score=Scoreboard()



screen.listen()
screen.onkey(my_player.up,"Up")
screen.onkey(my_player.right,"Right")
screen.onkey(my_player.leftDirection,"Left")
screen.onkey(my_player.down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    my_Car.create_cars()
    my_Car.move()

    # Dectecting the collision
    for car in my_Car.all_cars:
        if car.distance(my_player)<30:
            my_Score.game_over()  
            game_is_on=False

    if my_player.ycor()>280:
        my_player.goto(0,-280)
        my_Car.level_up()
        my_Score.increase_Score()

screen.exitonclick()