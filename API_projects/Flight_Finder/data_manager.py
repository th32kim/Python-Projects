import requests
from requests.auth import HTTPBasicAuth
SHEET_URL = "https://api.sheety.co/baf04cdc02f997c1e2524fedde840e82/copyOfFlightDeals/prices"
Sheet_update_url = "https://api.sheety.co/baf04cdc02f997c1e2524fedde840e82/copyOfFlightDeals/prices/"
SHEET_USER = "flight_test"
SHEET_PASS = "1234"

class DataManager:
    def __init__(self):
        self.update_IATA()
        self.pre_data()

    #function where it reads pre-defined data from the sheet
    def pre_data(self):
        self.sheet_init = requests.get(url = SHEET_URL, auth = HTTPBasicAuth(SHEET_USER,SHEET_PASS))
        self.sheet_init.raise_for_status()
        self.sheet_init_data = self.sheet_init.json()

    #function where it updates the sheet data, whenever a lowest price is detected
    def update_sheet(self, city, price):
        self.city = city
        self.l_price = str(price)
        self.city_id = 0
        for cities in self.sheet_init_data["prices"]:
            if cities["city"] == self.city.title():
                self.city_id = cities['id']
        self.param = {
            "price": {
                "lowestPrice": self.l_price
            }
        }
        self.sheet_update = requests.put(url = f"{Sheet_update_url}{self.city_id}",json = self.param, auth = HTTPBasicAuth(SHEET_USER,SHEET_PASS))
        self.sheet_update.raise_for_status()
        
    def update_IATA(self):
        for cities in self.sheet_init_data["prices"]:
            if cities["iataCode"] == "":
                # I_update = FlightSearch()
                # self.Iata = I_update.IATA_search(cities['city'])
                self.city_Id = cities['id']
                self.update_code = {
                    "price": {
                        "iataCode" : self.Iata
                    }
                }
                IATA_update = requests.put(url = f"{Sheet_update_url}{self.city}",json = self.update_code, auth = HTTPBasicAuth(SHEET_USER,SHEET_PASS))
                IATA_update.raise_for_status()
        
# # test_data = requests.get(url = SHEET_URL, auth = HTTPBasicAuth(SHEET_USER,SHEET_PASS))
# # test_data.raise_for_status()
# # data = test_data.json()
# # for cities in data["prices"]:
# #     if cities["city"] == "Toronto":
# #         print(cities['id'])
# # # changed_val_id = data["prices"][0]['id']
# # print(changed_val_id)
# param = {
#     "price": {
#         "lowestPrice": "2300"
#     }
# }

# test_update= requests.put(url = f"{Sheet_update_url}{2}",json = param, auth = HTTPBasicAuth(SHEET_USER,SHEET_PASS))
# test_update.raise_for_status()
# print(test_update)