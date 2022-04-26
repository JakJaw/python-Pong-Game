from turtle import Turtle


class Half(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pensize(4)
        self.color("white")
        self.hideturtle()

    def draw(self):
        self.goto(0, 400)
        self.right(90)
        for _ in range(12):
            self.pendown()
            self.forward(29)
            self.penup()
            self.forward(29)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score1 = 0
        self.score2 = 0

    def increase1(self):
        self.score1 += 1
        self.clear()
        self.write_score()
    def increase2(self):
        self.score2 += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=("Courier", 20, "normal"))

    def write_score(self):
        self.goto(-50, 220)
        self.write(self.score1, False, align="center", font=("Courier", 40, "normal"))
        self.goto(50, 220)
        self.write(self.score2, False, align="center", font=("Courier", 40, "normal"))