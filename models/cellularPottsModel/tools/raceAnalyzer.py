import sys
import csv
import numpy as np

deadCells = { 'count' : 0 }
means = []
totalCells = 0


def addPoints( data, deadCells, N ):
	spins = {str(i):[0] for i in range(1,N+1)}
	for i, row in enumerate(data):
		for x, spin in enumerate(row):
			if spin > 0:
				# if(spins.get(str(spin), 'na')):
				# 	spins[str(spin)] = []
				spins.get( str(spin) ).append( i )
	for k,v in spins.items():
		if len(v) == 1:
			deadCells['count'] += 1
	return spins

def averageMaxDistance(spins):
	mx = []
	for k,v in spins.items():
		mx.append( max(v) )
	return np.mean(mx)

fileNames = sys.argv[1:]

for fileName in fileNames:
	data = []
	with open(fileName, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		N = int(reader.next()[0])
		totalCells += N
		for row in reader:
			data.append(map(lambda x: int( float(x) ), row))
	means.append(averageMaxDistance(addPoints(data, deadCells, N)))

print 'total simulations=',len(fileNames)
print	'cell survival rate:',1-(deadCells['count']/float(totalCells))
print 'average max x=',np.mean(means)
print 'dt=',8000
print 'dx/dt=',(np.mean(means))/8000.0


# print data

