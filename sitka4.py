# Using the datetime module
# Adding dates to the x axis for the month of July 2018

import csv
import matplotlib.pyplot as plt
from datetime import datetime

infile = open("death_valley_2018_simple.csv", "r")
csvfile = csv.reader(infile)

header_row = next(csvfile)

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
lows = []
dates = []

mydate = datetime.strptime("2018-07-01", "%Y-%m-%d")
# print(mydate)

for row in csvfile:
    try:
        high = int(row[4])
        low = int(row[5])
        thedate = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {thedate}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(thedate)

# print(highs)

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.fill_between(dates, highs, lows, color="blue", alpha=0.1)

plt.title("Daily and low high temperatures - 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature(F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

fig.autofmt_xdate()

# plt.show()

plt.subplot(2, 1, 1)
plt.plot(dates, highs, c="red")
plt.title("Highs")

plt.subplot(2, 1, 2)
plt.plot(dates, lows, c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska")

plt.show()
