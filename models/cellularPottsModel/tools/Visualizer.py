import sys
import csv
import numpy as np
import matplotlib.pyplot as plt


fileName = str(sys.argv[1])


data = []
with open(fileName, 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		data.append(map(float, row))



plt.figure('Visualization of '+fileName)
plt.imshow(data, interpolation='nearest')
plt.colorbar(orientation='vertical')
plt.draw()
plt.show()