from turtle import Turtle
import random

COLORS = ["red", "blue", "cyan", "violet"]
Y_RANGE = [-230, 250]
X_RANGE = [-280, 280]

class Car(Turtle):
    def __init__(self, color_list=COLORS):
        super().__init__()
        self.shape("square")
        self.color(random.choice(color_list))
        self.penup()
        self.setheading(180)
        self.goto(random.randrange(X_RANGE[0], X_RANGE[1]), random.randrange(Y_RANGE[0], Y_RANGE[1]))
        self.shapesize(stretch_wid=1, stretch_len=2)

    def move(self):
        if self.xcor() < -280:
            self.goto(280, random.randrange(Y_RANGE[0], Y_RANGE[1]))
        else:
            new_x = self.xcor() - 10
            self.goto(new_x, self.ycor())