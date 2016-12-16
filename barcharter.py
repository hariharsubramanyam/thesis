import sys
import numpy as np
import matplotlib.pyplot as plt

fpath = sys.argv[1]
title = sys.argv[2]
xaxistitle = sys.argv[3]
f = open(fpath, "r")
lines = f.readlines()[1:]
f.close()

lines = [l.replace("\n", "") for l in lines]
lines = [l.split(",") for l in lines]
lines = [(a.strip(), b.strip(), float(c) / 1024.0) for (a, b, c) in lines]

plt.figure(figsize=(18, 10))
objects = [a + "-" + b for (a, b, c) in lines]
scaler = 1
y_pos = np.arange(0, len(objects) * scaler, scaler)
performance = [c for (a, b, c) in lines]
plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.autoscale(tight=True)
plt.yticks(y_pos, objects, fontsize=15)
plt.xticks(fontsize=20)
plt.xlabel(xaxistitle, fontsize=20)
plt.title(title, fontsize=30)
plt.show()

