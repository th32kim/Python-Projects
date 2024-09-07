from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    password_input.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
   
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password="".join(password_list[1:10])
    print(password)
    password_input.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_val = website_input.get()
    email_val = email_input.get()
    password_val = password_input.get()
    new_data = {
        website_val: {
            "email": email_val,
            "password": password_val
        }
    }

    if len(website_val)==0:
        messagebox.showwarning(message="Please enter your website")
        website_input.focus()
    elif len(email_val)==0:
        messagebox.showwarning(message="Please enter your email")
        email_input.focus()
    elif len(password_val)==0:
        messagebox.showwarning(message="Please enter your password")
        password_input.focus()
    else:
        is_ok=messagebox.askokcancel(title=website_val,message=f"These are the details entered: \nEmail:{email_val} \nPassword:{password_val} \n is it ok to save?")

        if is_ok:
            try:
                with open("tkinter_project/password_generator/data.json","r") as file:
                    #Reading old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("tkinter_project/password_generator/data.json","w") as file:
                    json.dump(new_data,file,indent=4)
            else: 
                json.update(new_data)
                with open("tkinter_project/password_generator/data.json","w") as file:
                    json.dump(data, file, indent=4)
            finally:
                #delete
                website_input.delete(0,END)
                password_input.delete(0,END)
# ---------------------------- JSON SEARCH ------------------------------- #   
def search():
    user_website = website_input.get()
    if len(user_website) != 0:
        try:
            with open("tkinter_project/password_generator/data.json","r") as file:
                data=json.load(file)
            email_info = data[user_website]["email"]
            password_info = data[user_website]["password"]
        except FileNotFoundError:
            messagebox.showwarning(message="The accounts do not exist, Please create a new account")
        except KeyError:
            messagebox.showwarning(message="The following website account does not exist, please check again")
        else:
            messagebox.showinfo(title="user-information",message = f"Information for {user_website} are \n Email: {email_info} \n Password: {password_info}")
    else:
        messagebox.showwarning(message="please input a value")
        website_input.focus()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width = 200, height = 200, highlightthickness=0 )
lock_image = PhotoImage(file="tkinter_project/password_generator/logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(column=1, row=0)

#Website
website_title = Label(text="Website: ")
website_title.grid(column=0, row=1)
website_input = Entry(width=26)
website_input.focus()
website_input.grid(column=1,row=1)
search_button = Button(text="Search",width=14,command=search)
search_button.grid(column=2,row=1)

#Email/Username
email_title = Label(text="Email/Username: ")
email_title.grid(column=0, row=2)
email_input = Entry(width=45)
email_input.insert(0,"dummy@email.com")
email_input.grid(column=1, row=2, columnspan=2)

#Password
password_title = Label(text="Password: ")
password_title.grid(column=0, row=3)
password_input = Entry(width=26)
password_input.grid(column=1,row=3)
generate_button = Button(text="Generate Password",command=password_gen)
generate_button.grid(column=2, row=3)

#Add button
add_button = Button(text="Add",width=38,command=save)
add_button.grid(column=1,row=4, columnspan = 2)

window.mainloop()