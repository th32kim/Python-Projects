# import smtplib

# my_email = "send.test02@gmail.com"
# password = "1234@asdf"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     #secure connection
#     connection.starttls()
#     #login
#     connection.login(user=my_email, password = password)
#     connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:Hello\n\nThis is the body of email")
#     connection.close()

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# print(year)

# date_of_birth = dt.datetime(year=,month=,day=)

import smtplib
import datetime as dt
import random

my_email = "send.test02@gmail.com"
password = "1234@asdf"

now = dt.datetime.now()
day_of_week = now.weekday()
monday = 0

if day_of_week == monday:
    with open("Send_email/quotes.txt") as quotes:
        list_quotes = quotes.readlines()
        quote = random.choice(list_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,msg=quote)
        connection.close()

