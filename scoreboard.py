from turtle import Turtle, right

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __int__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(0,270)
        self.increase=0
        self.updateScore()
        self.hideturtle()
    
    def updateScore(self):
        self.write(f"Level",align="right",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"Game over ☠️",align="right",font=FONT)

    def increase_Score(self):
        self.increase+=1
        self.clear()
        self.updateScore()    