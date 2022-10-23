from turtle import Turtle

class Game_score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_player_score = 0
        self.right_player_score = 0
        self.update_score()

    def update_score(self):

        self.goto(-100, 200)
        self.write(self.left_player_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right_player_score, align="center", font=("Courier", 80, "normal"))

    def increase_score_left(self):
        self.clear()
        self.left_player_score += 1
        self.update_score()


    def increase_score_right(self):
        self.clear()
        self.right_player_score += 1
        self.update_score()

