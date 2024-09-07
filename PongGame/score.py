from turtle import Turtle
FONT = ("Arial",40,"normal")

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.location = position
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(position)

        self.update_scoreboard()

    def add_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(self.score, align = "center", font =FONT )

    