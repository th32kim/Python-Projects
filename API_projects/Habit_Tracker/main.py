import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "heidlsyvhfy"
USER_NAME = "richard01"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}

# response = requests.post(url = pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_config, headers = headers)
# print(response.text)

today = datetime.now()

graph_update_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.74"
}

# graph_update = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
# response = requests.post(url = graph_update,json =graph_update_data,headers = headers )

parameter = {
    "quantity":"12.0"
}
# graph_date_update = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/20220531"
# response = requests.put(url = graph_date_update,json = parameter,headers = headers)
# print(response.text)
 
graph_delete = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/20220531"
response = requests.delete(url=graph_delete,headers = headers)
print(response.text)
