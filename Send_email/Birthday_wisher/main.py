import smtplib
import datetime as dt
import pandas
import random

my_email = "send.test02@gmail.com"
password = "1234@asdf"

today_tuple = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("Send_email/Birthday_wisher/birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"Send_email/Birthday_wisher/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email, to_addrs= my_email, msg=f"Subject:Happy Birthday \n\n {contents}")
    
