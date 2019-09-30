import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'

with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    dates, low_temp, high_temp = [], [], []

    for row in reader:
        try:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            low = int(row[3])
            high = int(row[1])
        except ValueError:
            print(str(date) + ' not found in weather history!!')
        else:
            dates.append(date)
            low_temp.append(low)
            high_temp.append(high)

figure = plt.figure(figsize=(12,8))
plt.title('Death Valley 2014 Weather History')
plt.plot(dates, low_temp, c='blue', alpha=0.5)
plt.plot(dates, high_temp, c='red', alpha=0.5)
plt.fill_between(dates, low_temp, high_temp, facecolor='blue', alpha=0.1)
plt.xlabel('', fontsize=14)
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=12)
figure.autofmt_xdate()
plt.show()
