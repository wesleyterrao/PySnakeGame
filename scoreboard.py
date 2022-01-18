from turtle import Turtle

POSITION = (0, 260)
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(POSITION)
        self.score = 0
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def show_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.show_score()