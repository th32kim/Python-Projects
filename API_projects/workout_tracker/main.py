import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
today = datetime.now()

today_date = today.strftime("%m/%d/%Y")
current_time = today.strftime("%H:%M:%S")
GENDER = "Male"
HEIGHT = 178
WEIGHT = 85
AGE = 22


API_ID = "26f8ba68"
API_KEY = "e6e811b4271ed1a4138bd3b15403f237"
NUT_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_API = "https://api.sheety.co/baf04cdc02f997c1e2524fedde840e82/myWorkoutsTest/workouts"
USER_NAME = 'test_workoutsheet'
PASSWORD = '1234'

headers = {
    "x-app-id":API_ID,
    "x-app-key":API_KEY,
    "x-remote-user-id":"0"
}
var_input = input("Tell me which exercises you did: ")

parameter = {
    "query": var_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

data_input = requests.post(url = NUT_URL, json = parameter, headers = headers )
data = data_input.json()
print(data)


for exercise in data["exercises"]:
    sheet_inputs={
        "workout":{
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url = SHEET_API, json = sheet_inputs,auth=HTTPBasicAuth(USER_NAME,PASSWORD))

