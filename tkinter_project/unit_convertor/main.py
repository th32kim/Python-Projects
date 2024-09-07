from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width =300, height=50)
window.config(padx=100,pady=200)
#Label
my_label = Label(text="is equal to", font=("Arial",12))
my_label.config(padx=5, pady=5)
my_label.grid(column=0,row=1)

#Button
def convert():
    user_input = float(input_miles.get())
    new_val = round(user_input*1.60934,2)
    km_label.config(text=new_val)
    

button = Button(text="calculate",command=convert)
button.config(padx=5, pady=5)
button.grid(column=1,row=2)


#Entry
input_miles = Entry(width=15)
input_miles.grid(column=1,row=0)
miles_label = Label(text="Miles",font=("Arial",12))
miles_label.config(padx=5,pady=5)
miles_label.grid(column=2,row=0)

#km label
km_label = Label(text="0", font=("Arial",12))
km_label.config(padx=5, pady=5)
km_label.grid(column=1, row=1)
km_text = Label(text="Km",font=("Arial",12))
km_text.config(padx=5,pady=5)
km_text.grid(column=2, row=1)



window.mainloop()