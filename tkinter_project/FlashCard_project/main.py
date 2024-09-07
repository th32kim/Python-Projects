from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- Functions ------------------------------- #
try :
    data = pandas.read_csv("tkinter_project/FlashCard_project/data/to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("tkinter_project/FlashCard_project/data/french_words.csv")
else:
    data = pandas.read_csv("tkinter_project/FlashCard_project/data/to_learn.csv")
finally:
    to_learn = data.to_dict(orient="records")
    current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    FlashCard.itemconfig(title_text,text="French",fill="black")
    FlashCard.itemconfig(word_text,text=current_card["French"])
    FlashCard.itemconfig(FlashCard_image,image=old_image)
    flip_timer = window.after(3000,func=flip)

def flip():
    global current_card
    FlashCard.itemconfig(FlashCard_image,image=new_image)
    FlashCard.itemconfig(title_text,text="English",fill="white")
    FlashCard.itemconfig(word_text,text=current_card["English"])

def is_known():
    global current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("tkinter_project/FlashCard_project/data/to_learn.csv", index=False)
    next_card()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip)

#FlashCard
FlashCard = Canvas(width = 800, height = 526, highlightthickness=0 )
old_image = PhotoImage(file="tkinter_project/FlashCard_project/images/card_front.png")
new_image = PhotoImage(file="tkinter_project/FlashCard_project/images/card_back.png")
FlashCard_image=FlashCard.create_image(400,263,image=old_image)
FlashCard.config(bg=BACKGROUND_COLOR)
FlashCard.grid(column=0, row=0,columnspan=2)

#Text
title_text = FlashCard.create_text(400,150,text="Title",font=("Arial",40,"italic"))
word_text = FlashCard.create_text(400,263,text="word",font=("Arial",60,"bold"))

#Buttons
wrong_image = PhotoImage(file="tkinter_project/FlashCard_project/images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.config(bg=BACKGROUND_COLOR)
wrong_button.grid(row=1,column=0)
right_image = PhotoImage(file="tkinter_project/FlashCard_project/images/right.png")
right_button = Button(image=right_image, highlightthickness=0,command=is_known)
right_button.config(bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()


