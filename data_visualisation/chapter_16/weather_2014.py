import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'

with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    dates, low_temp, high_temp = [], [], []
    for row in reader:
        dates.append(datetime.strptime(row[0], '%Y-%m-%d'))
        low_temp.append(int(row[3]))
        high_temp.append(int(row[1]))


fig = plt.figure(figsize=(12,8))
plt.title('Daily High Temperatures in 2014', fontsize=14)
plt.plot(dates, high_temp, c='red', alpha=0.5)
plt.plot(dates, low_temp, c='blue', alpha=0.5)
plt.fill_between(dates, high_temp, low_temp, facecolor='blue', alpha=0.1)
plt.xlabel('', fontsize=14)
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='minor', labelsize=14)
fig.autofmt_xdate()
plt.show()
