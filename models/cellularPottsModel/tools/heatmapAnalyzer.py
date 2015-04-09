import sys
import csv
import numpy as np
from matplotlib import rc

rc('text', usetex=True)

def nonZeroToOne(data):
	indicies = zip(*np.nonzero(data))
	for index in indicies:
		x,y = index
		data[x][y] = 1

fileNames = sys.argv[1:]

lattici = []

for fileName in fileNames:
	data = []
	with open(fileName, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		N = int(reader.next()[0])
		for row in reader:
			data.append(map(lambda x: int( float(x) ), row))
	lattici.append(data)

HEATMAP = np.zeros((len(lattici[0]), len(lattici[0])))

for lattice in lattici:
	nonZeroToOne(lattice)
	HEATMAP = HEATMAP + lattice

import matplotlib.pyplot as plt

plt.imshow(HEATMAP)
plt.title('Heatmap of finishing positions of 3-CTC races')
plt.xlabel('x positions')
plt.ylabel('y positions')
plt.show()