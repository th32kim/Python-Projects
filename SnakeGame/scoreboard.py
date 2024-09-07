from tkinter import CENTER
from turtle import Turtle

ALIGN = "center"
FONT = ("Arial",24,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("SnakeGame/high_score_storage.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.highscore}",align=ALIGN, font=FONT)


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("SnakeGame/high_score_storage.txt", mode = 'w') as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
        
    
    