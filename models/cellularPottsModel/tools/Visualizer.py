import sys
import csv
import numpy as np
import matplotlib.pyplot as plt


fileName = str(sys.argv[1])


data = []
with open(fileName, 'rb') as csvfile:
	reader = csv.reader(csvfile)
	N = int(reader.next()[0])
	for row in reader:
		data.append(map(float, row))

# NEW COLOR BAR
def discrete_cmap(N, base_cmap='jet'):
	if N == 1:
		return plt.cm.get_cmap('jet')
	base = plt.cm.get_cmap(base_cmap)
	color_list = base(np.linspace(0,1,N+1))
	# print color_list
	cmap_name = base.name+str(N)
	return base.from_list(cmap_name, color_list, N+1)

plt.figure('Visualization of '+fileName)
plt.imshow(data, interpolation='nearest', cmap=discrete_cmap(N))
plt.colorbar(orientation='vertical', ticks=range(N+1))
plt.draw()
plt.show()
print 'Complete'