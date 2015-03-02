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
# print 'x.size=',x.size
#initialize with 1 cell

x.initialize(4)
y = x.deepCopy()
print 'x.matrix=',x.matrix
print 'y.matrix=',y.matrix

# prior = Heatmap(z=x.matrix.tolist())

print 'running simulation for 3 MCS using moore'
x.runSimulation(20)
y.runSimulation(20, 'neumann')
print 'x.matrix=',x.matrix
print 'y.matrix=',y.matrix


# moore = Heatmap(
# 	z=x.matrix.tolist(),
# 	name='Moore Neighbourhood'
# )
# neumann = Heatmap(
# 	z=y.matrix.tolist(),
# 	name='Von Neumann Neighbourhood',
# 	xaxis='x2',
# 	yaxis='y2'
# )

#print str(ds.Tools.rndm(5,10))
#print 'running probability with p=0.25'
#for i in range(1,10):
#    print str(ds.Tools.probability(0.25))
#print 'running probability with p=0.9'
#for i in range(1,10):
#    print str(ds.Tools.probability(0.9))

# data = Data([moore, neumann])

# fig = pltls.get_subplots(rows=1, columns=2)
# fig['data'] += data
# fig['layout'].update(title='Comaprison of Moore and Von Neumman neighbourhood strategies in Simulation')

# plot_url = pltly.plot(fig, filename='comaprison-moore-neumann')

# plot_url = pltly.plot(fig, filename='simulation')


#testing for cells.
cell1 = ds.Cell(1)
cell2 = ds.Cell(1)
cell3 = ds.Cell(2)

print 'the following should print the same thing on two lines:'
print str(x.interactionStrength(cell1,cell3))
print str(x.interactionStrength(cell3,cell1))
print 'this should be different'
print str(x.interactionStrength(cell1,cell2))

