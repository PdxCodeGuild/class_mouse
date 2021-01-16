import requests, math, re
# import statistics
from numpy import ma
from datetime import datetime
from rain_data import RainData
import matplotlib.pyplot as plt


url = "https://or.water.usgs.gov/non-usgs/bes/swan_island_pump.rain"

response = requests.get(url)

data = response.text

# all_dates = re.findall(r'\d{2}-[A-Z]+-\d{4}\s+\d+', data)
# rain_amounts = re.findall(r'\d{4}\s+(\d*-?)\s+', data)

data = re.findall(r'(\d+-\w+-\d+)\s+(\d+)', data)

days_of_rain = []
total_tips = 0
for day in data:
    total_tips += int(day[1])
    date = datetime.strptime(day[0], '%d-%b-%Y')
    days_of_rain.append(RainData(date, int(day[1])))


most_rain = days_of_rain[0]
for day in days_of_rain:
    if day.tips > most_rain.tips:
        most_rain = day

# variance = statistics.variance([day.tips for day in days_of_rain])
variance = ma.var([day.tips for day in days_of_rain])
# print(variance)
# std_dev = statistics.stdev([day.tips for day in days_of_rain])
mean = total_tips / len(days_of_rain)

print(f"Start: {days_of_rain[0].date} End: {days_of_rain[-1].date} Variance: {variance} Mean: {mean} Day with most rain: {most_rain.date} with {most_rain.inches} inches")
plt.plot([day.date for day in days_of_rain], [day.inches for day in days_of_rain])
plt.show()