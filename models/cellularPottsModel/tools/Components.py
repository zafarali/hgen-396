import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
from Tools import Tools

def numberOfComponents( data, N ):
	# create a matrix of zeros
	# to store the graph
	G = np.zeros((N,N))

	isEdgeCase = lambda x,y: Tools.isEdgeCase(x, y, 0, len(data))

	# loop through all the lattice positions
	for x in range( len( data ) ):
		for y in range( len( data[x] ) ):
			# obtain neighbours of selected position
			neighbours = Tools.getNeighbourIndices( x , y , method='neumann')

			# loop through all neighbours
			for neighbour in neighbours:
				nx,ny = neighbour

				#check if this neighbour is an edge case
				if not isEdgeCase( nx, ny ):
					# print 'not edge case'
					if data[x][y] != 0 and data[nx][ny] != 0 :
						print data[x][y], data[nx][ny]
					# if the spins in each position are different and non zero
					if ( data[x][y] != data[nx][ny] ) and ( ( data[x][y] != 0 ) and ( data[nx][ny] != 0 ) ):
						# obtain the 'spin'/'node' 
						# convert it to an index for the graph G.
						node1 = int(data[x][y]) - 1
						node2 = int(data[nx][ny]) - 1
						G[node1][node2] = 1
						G[node2][node1] = 1
	print G
	# create a sparse graph
	graph = sparse.csr_matrix(G)
	# do connected components analysis
	print sparse.csgraph.connected_components(graph, directed=False)


if __name__ == '__main__':
	fileName = str(sys.argv[1])
	data = []
	with open(fileName, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		N = int(reader.next()[0])
		for row in reader:
			data.append(map(lambda x: int( float(x) ), row))

	numberOfComponents( data, N )
