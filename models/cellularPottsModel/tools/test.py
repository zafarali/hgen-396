__author__ = 'zafarali'
#To change this template use Tools | Templates.
#
#

## plotting stuff
# import plotly.plotly as pltly
# from plotly.graph_objs import *
# import plotly.tools as pltls

import ds

x = ds.Lattice(20)
print 'x.size=',x.size
#initialize with 1 cell

x.initialize(10)
print 'x.matrix=',x.matrix

# prior = Heatmap(z=x.matrix.tolist())

print 'running simulation for 3 MCS'
x.runSimulation(20)
print 'x.matrix=',x.matrix


# prosterior = Heatmap(z=x.matrix.tolist())


#print str(ds.Tools.rndm(5,10))
#print 'running probability with p=0.25'
#for i in range(1,10):
#    print str(ds.Tools.probability(0.25))
#print 'running probability with p=0.9'
#for i in range(1,10):
#    print str(ds.Tools.probability(0.9))

# data = Data([prior])
# fig = Figure(data=data)
# data2 = Data([prosterior])
# fig2 = Figure(data=data2)
# plot_url = pltly.plot(fig, filename='simulation-before')
# plot_url2 = pltly.plot(fig2, filename='simulation-after')


#testing for cells.
cell1 = ds.Cell(1)
cell2 = ds.Cell(1)
cell3 = ds.Cell(2)

print 'the following should print the same thing on two lines:'
print str(x.interactionStrength(cell1,cell3))
print str(x.interactionStrength(cell3,cell1))
print 'this should be different'
print str(x.interactionStrength(cell1,cell2))

