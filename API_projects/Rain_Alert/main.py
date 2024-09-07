api_key = "69f04e4613056b159c2761a9d9e664d2"
import requests
import smtplib

my_email = "send.test02@gmail.com"
password = "1234@asdf"
message = ""

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": 37.566536,
    "lon": 126.977966,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}

data = requests.get(url=OWM_Endpoint,params = parameters)
data.raise_for_status()
weather_data = data.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    message = "Bring your Umbrella!"
else:
    message = "Umbrella not needed!"


with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject: Weather Forecast \n\n {message}")
        connection.close()



