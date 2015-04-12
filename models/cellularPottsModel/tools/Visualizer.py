import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

# rc('text', usetex=True)


def Visualizer( data, N, name ):
	# NEW COLOR BAR
	def discrete_cmap(N, base_cmap='prism'):
		if N == 1:
			return plt.cm.get_cmap('jet')
		base = plt.cm.get_cmap(base_cmap)
		color_list = base(np.linspace(0,1,N+1))
		color_list[0] = (.5,.5,.5,1.0)
		# print color_list
		cmap_name = base.name+str(N)
		return base.from_list(cmap_name, color_list, N+1)

	plt.figure('Visualization of '+name)
	plt.imshow(data, interpolation='nearest', cmap=discrete_cmap(N))
	cbar = plt.colorbar(orientation='vertical', ticks=range(N+1))
	cbar.ax.set_ylabel('Cell $\sigma$')
	plt.title('Lattice')
	plt.xlabel('x position')
	plt.ylabel('y position')
	plt.draw()
	plt.show()
	print 'Complete'

if __name__ == '__main__':
	fileNames = sys.argv[1:]
	for fileName in fileNames:
		data = []
		with open(fileName, 'rb') as csvfile:
			reader = csv.reader(csvfile)
			N = int(reader.next()[0])
			for row in reader:
				data.append(map(float, row))
		Visualizer(data, N, fileName)
