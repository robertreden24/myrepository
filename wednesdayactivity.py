import csv
from matplotlib import pyplot as plt
import statistics as stat

filename = "activity.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    date_steps = {}
    dict_interval = {}

    for row in reader:
        steps = row[0]

        if steps != "NA":
            date = row[1]
            interval = int(row[2])

            date_steps.setdefault(str(date), [])
            date_steps[str(date)].append(int(steps))
            dict_interval.setdefault(interval, [])
            dict_interval[interval].append(int(steps))

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