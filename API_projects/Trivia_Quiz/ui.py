from tkinter import *
from turtle import bgcolor
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        #Scoreboard
        self.scoreboard = Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.scoreboard.grid(column=1,row=0)

        #Question Box
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,125,width=280,text="Hello World", fill=THEME_COLOR, font=("Arial",20,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        #Buttons
        self.right_image = PhotoImage(file="API_projects/Trivia_Quiz/images/true.png")
        self.right_button = Button(image=self.right_image,highlightthickness=0,command=self.true_pressed)
        self.right_button.grid(column=0,row=2)
        self.wrong_image = PhotoImage(file="API_projects/Trivia_Quiz/images/false.png")
        self.wrong_button = Button(image=self.wrong_image,highlightthickness=0,command=self.false_pressed)
        self.wrong_button.grid(column=1,row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.scoreboard.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've Completed")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)


    def false_pressed(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)


    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)
    
    

        
        
    