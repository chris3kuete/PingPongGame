from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.penup()
        self.x_move = 0.7
        self.y_move = 0.7
        self.ball_speed = 0.004

    def ball_move(self):
        newX = self.xcor() + self.x_move
        newY = self.ycor() + self.y_move
        self.goto(newX, newY)

    def bounce_back_y(self):
        self.y_move *= -1

    def bounce_back_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.005

    def reset_ball(self):
        self.x_move *= -1
        self.ball_speed = 0.004
        self.goto(0, 0)



