import turtle
from text import Text

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
text = Text()

end_game = False
while not end_game:
    answer_state = screen.textinput(title=f"{text.score}/50", prompt = "What's another State's name? ").title()
    text.answer_check(answer_state)
    if text.score == 50:
        end_game = True
    if answer_state == "Exit":
        text.lesson()


turtle.exitonclick()