from turtle import Turtle, Screen, time
from paddle import Paddle
from ball import Ball
from score import Score
import time
import keyboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_1_POS = (SCREEN_WIDTH/2 - 50,0)
PADDLE_2_POS = (-1*(SCREEN_WIDTH/2 - 50),0)
#if it reaches 10, game over
end_game = False

#screen set up
screen = Screen()
screen.title("PongGame")
screen.setup(width = SCREEN_WIDTH,height = SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

#game components setup
paddle_1 = Paddle(PADDLE_1_POS)
paddle_2 = Paddle(PADDLE_2_POS)
score_1 = Score((40,240))
score_2 = Score((-40,240))
ball = Ball()

#game control setup
screen.listen()

screen.onkey(paddle_1.up,"Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up,"w")
screen.onkey(paddle_2.down,"s")

#game algorithm
def game_reset():
    ball.reset()
    paddle_1.reset()
    paddle_2.reset()

while not end_game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
   
    #checking if the ball have reached the top
    if ball.ycor()>(SCREEN_HEIGHT/2) - 20 or ball.ycor()<(SCREEN_HEIGHT/2)*-1 + 20:
        ball.bounce_y()
    
    #checking if the ball bouces with the paddle
    if ball.xcor()>(SCREEN_WIDTH/2)-80 and ball.distance(paddle_1)<50 or ball.xcor()<-(SCREEN_WIDTH/2-80) and ball.distance(paddle_2)<50:
        ball.bounce_x()

    #check if the ball goes outside the range , score check
    if ball.xcor()>(SCREEN_WIDTH/2)-20:
        score_2.add_score()
        game_reset()
    elif ball.xcor()<((SCREEN_WIDTH/2)-20)*-1:
        score_1.add_score()
        game_reset()
    
    

screen.exitonclick()


