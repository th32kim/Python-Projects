from turtle import Turtle
import time
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.paddle_position = position
        self.penup()
        self.shapesize(stretch_wid = 5, stretch_len=1, outline = None)
        self.goto(self.paddle_position)

    def reset(self):
        self.goto(self.paddle_position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
        
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
    
    
    
            

