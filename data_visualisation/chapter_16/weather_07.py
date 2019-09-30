import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'

with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    dates, low_temp, high_temp = [], [], []
    for row in reader:
        dates.append(datetime.strptime(row[0], '%Y-%m-%d'))
        low_temp.append(int(row[3]))
        high_temp.append(int(row[1]))




fig = plt.figure(figsize=(10,6))
plt.title('Daily High Temperatures in July of 2014', fontsize=14)
plt.plot(dates, high_temp, c='red')
plt.xlabel('', fontsize=14)
plt.ylabel('Maximum Temperature', fontsize=14)
plt.tick_params(axis='both', which='minor', labelsize=14)
fig.autofmt_xdate()
plt.show()



"""
#enumerate(list) returns a tuple of (index, value)
for index, column_header in enumerate(header_row):
    print(index, column_header)


#strptime(date_string, date_format) and returns a sexy date format
from datetime import datetime
first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
"""
