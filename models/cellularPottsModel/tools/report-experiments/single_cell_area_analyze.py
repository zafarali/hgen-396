import numpy as np
import matplotlib.pyplot as plt
import csv

# read in cells
with open('./final_cell_areas_start1.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	allCells = reader.next()

# all cells
allCells = map(int,allCells)

# cells which have no died
nonZero = [ i for i in allCells if i !=0 ]

# plotting
fig1 = plt.figure('Final Cell Areas')
bins = range(0,60)
plt.hist(nonZero, bins, alpha=0.5)
plt.xlabel('Final Cell Areas')
plt.ylabel('Frequency')
plt.title('Distribution of Final Cell Areas, T=250MCS')
fig1.hold()
fig1.show()

raw_input()
print 'total cells:', len(allCells)
print 'total died:', len(allCells)-len(nonZero)
print 'mean non-zero cell area:', np.mean(nonZero)
print 'variance in non-zero cell area:', np.var(nonZero)