import matplotlib.pyplot as plt
import numpy as np

f = open("times_for_methods.csv", "r")
lines = f.readlines()[1:]
f.close()
lines = [l.replace("\n", "") for l in lines]
lines = [tuple(l.split(",")) for l in lines]
lines = [(a, b, float(c)) for (a, b, c) in lines]

data_for_key = {}
for line in lines:
    key = line[0]
    if key not in data_for_key:
        data_for_key[key] = [[], []]
    data_for_key[key][0].append(line[1])
    data_for_key[key][1].append(line[2])

keys = data_for_key.keys()

num_plots = len(keys)

colormap = plt.cm.gist_ncar
plt.figure(figsize=(18, 10))
plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, num_plots)])
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Number of Times Each Row was Duplicated', fontsize=20)
plt.ylabel('Runtime (ms)', fontsize=20)

for key in keys:
    plt.plot(data_for_key[key][0], data_for_key[key][1], linewidth=3)
plt.legend(keys, loc='upper left', bbox_to_anchor=(0.0, 0.63))
plt.title("API Method Runtime vs. Number of Duplications", fontsize=30)

plt.show()

