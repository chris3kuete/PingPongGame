from turtle import Screen
from pad1 import Pad1
from pad2 import Pad2
from ball import Ball
import time
from score import Game_score


POINT = 0



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Ping Pong Game")
screen.tracer(0)

racket_ball1 = Pad1()
racket_ball2 = Pad2()
tennis_ball = Ball()
scoreboard = Game_score()

screen.listen()
screen.onkey(racket_ball1.up, "o")
screen.onkey(racket_ball1.down, "l")

screen.onkey(racket_ball2.up, "u")
screen.onkey(racket_ball2.down, "j")

screen_is_on = True

while screen_is_on:
    time.sleep(tennis_ball.ball_speed)
    screen.update()
    tennis_ball.ball_move()

    #this detect collision with the wall
    if tennis_ball.ycor() > 280 or tennis_ball.ycor() < -280:
        tennis_ball.bounce_back_y()

    #Detect collision with the pad
    if tennis_ball.distance(racket_ball1) < 50 and tennis_ball.xcor() > 320:
        tennis_ball.bounce_back_x()

    if tennis_ball.distance(racket_ball2) < 50 and tennis_ball.xcor() < -320:
        tennis_ball.bounce_back_x()

    #When player miss the ball,detect collision with the wall
    if tennis_ball.xcor() > 380:
        scoreboard.increase_score_left()
        tennis_ball.reset_ball()


    if tennis_ball.xcor() < -380:
        scoreboard.increase_score_right()
        tennis_ball.reset_ball()


screen.exitonclick()
