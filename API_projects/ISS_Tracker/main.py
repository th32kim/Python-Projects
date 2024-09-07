import requests
from datetime import datetime
import smtplib
import time
MY_EMAIL = "send.test02@gmail.com"
PASSWORD = "1234@asdf"
MY_LAT = 37.566536 # Your latitude
MY_LONG = 126.977966 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json() 

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def iss_above():
    if MY_LAT-5<=iss_latitude< MY_LAT+5 and MY_LONG-5<=iss_longitude<MY_LONG+5:
        return True
    else:
        return False

def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        message = "Look up, there is an ISS passing"
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg =f"Subject: ISS \n\n {message}" )
        connection.close()


def is_night():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    time_now = time_now.hour

    if time_now >= sunset or time_now <=sunrise:
        return True
    else:
        return False

print(data)
# while True:
#     time.sleep(60)
#     if iss_above() and is_night():
#         send_mail()

