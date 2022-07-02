
from hashlib import new
from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)
    
    def up(self):
        self.forward(MOVE_DISTANCE)
    def down(self):
        self.backward(MOVE_DISTANCE)
    def right(self):
        new_x=self.xcor()+MOVE_DISTANCE
        self.goto(new_x,self.ycor())
    def leftDirection(self):
        new_x=self.xcor()-MOVE_DISTANCE
        self.goto(new_x,self.ycor())
