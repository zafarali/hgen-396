import sys, csv, datetime
import numpy.random as random
startTime = datetime.datetime.now()

'''
@version 0.0.2
@author Zafarali Ahmed
@args Number of cells
@args Mean Dissociation constant
@args Standard deviation of Dissociation constant
@args Number of Observations needed
@args@optional Output File (default: output.csv)
'''

print 'You are only strong as your weakest link'

requiredArguments = 6

##Checking for enough number of arguments
if len(sys.argv)<3:
	print 'Please input the minimum number of arguments as follows:'
	print 'argv[1] # of cells'
	print 'argv[2] mean dissociation constant'
	print 'argv[3] standard deviation of constant'
	print 'argv[4] # of enumerations'
	print 'argv[5] optional output file.'
	sys.exit()

#variable assignment
numCells, meanKd, sdKd, enumerations = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

#deciding output file
outputFile = 'output.csv' if not len(sys.argv) == requiredArguments else sys.argv[requiredArguments-1]

f = open(outputFile, 'wt')
try:
	writer = csv.writer(f)
	writer.writerow( ['highestKd', 'sizeA','sizeB'] )
except IOError:
	print 'something went wrong trying to open this file'


value = random.normal(meanKd, sdKd);

for i in range(0,int(enumerations)):
	# range over the number of observations you want
	highestKd = float(meanKd)
	cellOfHighestKd = 0

	#range over the number of cells in your string
	for j in range(0, int(numCells)):
		thisKd = random.normal(float(meanKd), float(sdKd))

		#checking if the new kd is higher than what we already have
		if thisKd > highestKd:
			highestKd = thisKd
			cellOfHighestKd = j

	#write the data collected
	try:
		writer = csv.writer(f)
		sizeA = int(cellOfHighestKd) - 1
		sizeB = int(numCells) - int(cellOfHighestKd)
		writer.writerow([highestKd,sizeA,sizeB])
	except IOError:
		print 'cannot write'


f.close()

print str('Took'), datetime.datetime.now()- startTime,'ms to complete'