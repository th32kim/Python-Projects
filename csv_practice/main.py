import pandas

# data = pandas.read_csv("Users\Richard\OneDrive\Desktop\Project\Python Udemy\csv_practice\weather_data.csv")
# data_dict = data.to_dict()

# temp_list = data["temp"].to_list()

# max_value = data["temp"].max()



# #get data in the rows
# monday= (data[data.day=="Monday"])
# monday_temp = int(monday.temp)*1.8 + 32
# print(monday_temp)


# #create a dataframe from a scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [75, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("Users\Richard\OneDrive\Desktop\Project\Python Udemy\csv_practice\ new_data.csv")
fur_color = ["grey", "red", "black"]

data = pandas.read_csv("Users\Richard\OneDrive\Desktop\Project\Python Udemy\csv_practice\squirell_data.csv")
grey = len(data[data['Primary Fur Color']=='Gray'])
red = len(data[data['Primary Fur Color']=='Red'])
black = len(data[data['Primary Fur Color']=='Black'])

Count = [grey, red, black]
print(grey)
final_dic = {
    "Furcolor": fur_color,
    "Count": Count
}

df = pandas.DataFrame(final_dic)
df.to_csv("Users\Richard\OneDrive\Desktop\Project\Python Udemy\csv_practice\squirell_count.csv")