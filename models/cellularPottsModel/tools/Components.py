import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
from Tools import Tools

def numberOfComponents( data, N ):
	# create a matrix of zeros
	# to store the graph

	isEdgeCase = lambda x,y: Tools.isEdgeCase(x, y, 0, len(data))

	edgeList = []

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
					# if the spins in each position are different and non zero
					# if ( data[x][y] != data[nx][ny] ) and ( ( data[x][y] != 0 ) and ( data[nx][ny] != 0 ) ):
					if ( data[x][y] != data[nx][ny] ):
						# obtain the 'spin'/'node' 
						# convert it to an index for the graph G.
						node1 = int(data[x][y])
						node2 = int(data[nx][ny])
						edgeList.append( ( node1, node2 ) )
						edgeList.append( ( node2, node1 ) )

	import itertools

	# create a list of nodes from the edge list
	nodeList = list( set( list( itertools.chain( *edgeList ) ) ) )
	# number of non-zero nodes
	nbNodes = len( nodeList ) - 1
	G = np.zeros( ( nbNodes , nbNodes) )

	for e in edgeList:
		u,v = e
		# if both incoming and outgoing are not-zero we populate
		# G with 1s, else we don't
		if u != 0 and v != 0 :
			i = nodeList.index(u)-1
			j = nodeList.index(v)-1
			G[i][j] = 1
			G[j][i] = 1

	# create a sparse graph
	graph = sparse.csr_matrix(G)
	# do connected components analysis
	y,_ = sparse.csgraph.connected_components(graph, directed=False)
	return y-1 if y > 1 else 0


if __name__ == '__main__':
	fileNames = sys.argv[1:]
	total = 0
	for fileName in fileNames:
		data = []
		with open(fileName, 'rb') as csvfile:
			reader = csv.reader(csvfile)
			N = int(reader.next()[0])
			for row in reader:
				data.append(map(lambda x: int( float(x) ), row))
		total = total + numberOfComponents( data, N )
		print total
