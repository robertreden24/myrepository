import csv
import matplotlib.pyplot as plt
import statistics as stat

filename = "activity.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    with open("completeValues.csv", "w") as new_file:

        new_file.write(str(header[0]) + "," + str(header[1]) + "," + str(header[2]))
        new_file.write("\n")

        n = 0
        for row in reader:

            if row[0] == "NA":
                row[0] = 0
                n += 1

            new_file.write(str(row[0]) + "," + str(row[1]) + "," + str(row[2]))
            new_file.write("\n")

        print("Total numbers of missing values in the dataset is " + str(n))


new_filename = "completeValues.csv"
with open(new_filename) as nf:
    reader = csv.reader(nf)
    header = next(reader)

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