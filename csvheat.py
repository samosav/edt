import csv
import numpy as np

iniArray = np.random.uniform(0,4,[8,8])
data = np.array([x for x in iniArray.reshape(iniArray.size)])
data = data.reshape(iniArray.shape)

with open('plot.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)
