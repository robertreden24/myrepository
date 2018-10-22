import csv
from matplotlib import pyplot as plt
import statistics as stat
import datetime

filename = "activity.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    date_steps = {}
    dict_interval = {}
    interval_weekdays = {}
    interval_weekends = {}

    for row in reader:
        steps = row[0]

        if steps != "NA":
            date = row[1]
            date_format = datetime.datetime.strptime(date, "%Y-%m-%d")
            interval = int(row[2])

            date_steps.setdefault(str(date), [])
            date_steps[str(date)].append(int(steps))
            dict_interval.setdefault(interval, [])
            dict_interval[interval].append(int(steps))
            
            if date_format.isoweekday() == 6 or date_format.isoweekday() == 7:
                interval_weekends.setdefault(interval, [])
                interval_weekends[interval].append(int(steps))
            else:
                interval_weekdays.setdefault(interval, [])
                interval_weekdays[interval].append(int(steps))

list_date = []
total = []
average = []

for i in date_steps.keys():
    list_date.append(i)
    total.append(sum(date_steps.get(i)))
    average.append(stat.mean(date_steps.get(i)))

plt.hist(total)
plt.title("Total Steps per day")
plt.xlabel("Steps per day")
plt.ylabel("Frequency")
plt.yticks(range(0, 25, 5))
plt.show()

print("Mean : " + str(stat.mean(total)))
total_sort = sorted(total)
print("Median : " + str(stat.median(total_sort)))

averageStepsPerInterval = []

for i in dict_interval.keys():
    averageStepsPerInterval.append(stat.mean(dict_interval.get(i)))

fig = plt.figure(dpi=90, figsize=(13, 5))

plt.plot(list(dict_interval.keys()), averageStepsPerInterval, c = "blue")
plt.title("Average daily activity")
plt.xlabel("Time Interval")
plt.ylabel("Average number of steps taken")
plt.show()

max_steps = max(averageStepsPerInterval)
max_index = averageStepsPerInterval.index(max_steps)

Max = ""
n = 0

for i in dict_interval.keys():
    if n == max_index:
        Max = i
        break
    n += 1

print("Maximum number of steps is in interval " + str(Max))

weekdays = []
weekends = []

for i in interval_weekdays.keys():
    weekdays.append(stat.mean(interval_weekdays.get(i)))

for i in interval_weekends.keys():
    weekends.append(stat.mean(interval_weekends.get(i)))

fig = plt.figure(dpi=90, figsize=(15, 5))

plt.plot(list(dict_interval.keys()), weekdays, color='blue', label='Weekdays')
plt.plot(list(dict_interval.keys()), weekends, color='red', label='Weekend')
plt.legend(loc='upper right')
plt.title("All Weekdays and Weekends")
plt.xlabel("Time Interval")
plt.ylabel("Average number of steps taken")
plt.show()
