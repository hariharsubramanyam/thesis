import matplotlib.pyplot as plt
import numpy as np

f = open("time_overhead.csv", "r")
lines = f.readlines()[1:]
f.close()
lines = [l.replace("\n", "") for l in lines]
lines = [tuple(l.split(",")) for l in lines]
lines = [(a, b, float(c), 100 * float(d)) for (a, b, c, d) in lines]

data_for_key = {}
for line in lines:
    key = (line[0], line[1])
    if key not in data_for_key:
        data_for_key[key] = [[], []]
    data_for_key[key][0].append(line[2])
    data_for_key[key][1].append(line[3])

keys = data_for_key.keys()
x = np.arange(10)

plt.figure(figsize=(18, 10))
plt.gca().set_color_cycle(['red', 'orange', 'gold', 'green', 'blue', 'indigo', 'violet', 'black', 'cyan'])
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Number of Rows in Dataset', fontsize=20)
plt.ylabel('Time Overhead (% of overall runtime)', fontsize=20)

for key in keys:
    plt.plot(data_for_key[key][0], data_for_key[key][1], linewidth=3)


keyStrings = [key[0] + "-" + key[1] for key in keys]
plt.legend(keyStrings, loc='upper right')
plt.title("Time Overhead vs. Dataset Size", fontsize=30)

plt.show()
