from turtle import Turtle


POSITION = (0, 265)
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.score = 0
        self.remaining_bots = 15

    def show_score(self):
        self.write(f"score: {self.score} - remaining bots: {self.remaining_bots}", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.remaining_bots -= 1
        self.write(f"score: {self.score} - remaining bots: {self.remaining_bots}", align=ALIGNMENT, font=FONT)
