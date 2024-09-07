from turtle import Turtle
import pandas
STATE_DATA = "us-states-game-start/50_states.csv"
all_state = []

class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.score = 0
        self.hideturtle()

    def answer_check(self, user_input):
        self.user_answer = user_input
        self.states = pandas.read_csv(STATE_DATA)
        self.states_list = self.states.state.to_list()
        count = len(self.state[self.state["state"]==self.user_answer])
        if count == 1:
            self.display_text()

    def display_text(self):
        if self.user_answer not in all_state:
            answer = self.state[self.state["state"]==self.user_answer]
            xcor = int(answer.x)
            ycor = int(answer.y)
            state_answer = self.user_answer
            self.setposition(xcor,ycor)
            self.write(state_answer)
            self.score_increase()
            all_state.append(self.user_answer)
        else:
            print("already tried that idiot")

    def score_increase(self):
        self.score+=1
    

    