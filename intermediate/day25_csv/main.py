# with open("weather_data.csv") as weather:
#     weather_rows = [row.strip() for row in weather.readlines()]
#     print(weather_rows)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# Get data in a column - using dot notation works because it converts the columns into object attributes.
# Can also be accessed via bracket notation: print(data["temp"])
# print(data.temp)
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # avg_temp = sum(temp_list)/len(temp_list)
# # print(avg_temp)
# print(data["temp"].mean())
#
# print(data["temp"].max())

# Get hold of a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# Select a row based on index
# print(data.iloc[[1]])

# Select a row by index and a specific value in that row
# print(data.iloc[1].day)

# Convert Monday's temperature to Fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")