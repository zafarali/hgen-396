# load the data
import csv
with open('performance2.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	info = map(float,reader.next())
print info
# do the plotting
import matplotlib.pyplot as plt

plt.plot(range(1,len(info)+1), info)
plt.title('Running Time of CPM Model for 1000 MCS')
plt.xlabel('Lattice Size')
plt.ylabel('Running Time (seconds)')
plt.show()
raw_input()