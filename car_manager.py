from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_Speed=STARTING_MOVE_DISTANCE

    def create_cars(self):
        # TO reduce the chnaces of creteing an random car we create a random no from 1  in 6
        random_chances= random.randint(1,8)
        if random_chances ==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=3,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)    
            self.all_cars.append(new_car)

    # Moving the car across the screen
    def move(self):
        for car in self.all_cars:
            car.backward(self.car_Speed)

    # level up when the tutrle reach the final line 

    def level_up(self):
        self.car_Speed+=2
        


    