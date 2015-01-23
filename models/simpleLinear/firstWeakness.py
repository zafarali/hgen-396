import sys, csv, datetime
import numpy.random as random
startTime = datetime.datetime.now()

'''
First Weakness Model
The string of cells will break at the location at the first 
Kd which is above the threshold.
@version 0.0.1
@author Zafarali Ahmed
@args Number of cells
@args Mean Dissociation constant
@args Standard deviation of Dissociation constant
@args Kd Threshold
@args Number of Observations needed
@args@optional Output File (default: output.csv)
'''

requiredArguments = 7

##Checking for enough number of arguments
if len(sys.argv)<6:
	print 'Please input the minimum number of arguments as follows:'
	print 'argv[1] # of cells'
	print 'argv[2] mean dissociation constant'
	print 'argv[3] standard deviation of constant'
	print 'argv[4] threshold'
	print 'argv[5] # of enumerations'
	print 'argv[6] optional output file.'
	sys.exit()

#variable assignment
numCells, meanKd, sdKd, thresholdKd, enumerations = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]

#deciding output file
outputFile = 'output.csv' if not len(sys.argv) == requiredArguments else sys.argv[requiredArguments-1]

f = open(outputFile, 'wt')
try:
	writer = csv.writer(f)
	writer.writerow( ['KdOfBrokenLink', 'thresholdKd', 'sizeA', 'sizeB'] )
except IOError:
	print 'something went wrong trying to open this file'


value = random.normal(meanKd, sdKd);

for i in range(0,int(enumerations)):
	# range over the number of observations you want
	highestKd = float(meanKd)
	brokenLink = 0
	broken = 0
	#range over the number of cells in your string
	for j in range(0, int(numCells)):
		thisKd = random.normal(float(meanKd), float(sdKd))

			#checking if the new kd is higher than what we already have
		if float(thisKd) > float(thresholdKd):
			highestKd = thisKd
			brokenLink = j
			break

	#write the data collected
	try:
		writer = csv.writer(f)
		sizeA = 0 if int(brokenLink) == 0 else int(brokenLink)-1
		sizeB = int(numCells) - int(brokenLink)
		highestKd = 0 if float(highestKd)==float(meanKd) else highestKd
		writer.writerow([highestKd,thresholdKd, sizeA, sizeB])

	except IOError:
		print 'cannot write'


f.close()

print str('Took'), datetime.datetime.now()- startTime,'ms to complete'