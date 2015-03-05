__author__ = 'zafarali'
#To change this template use Tools | Templates.
#
#

## plotting stuff
# import plotly.plotly as pltly
# from plotly.graph_objs import *
# import plotly.tools as pltls

import ds
from EnergyFunction import EnergyFunction

energies = {
	'2': (1,1),
	'11': (1,2),
	'14': (2,2),
	'16': (2,0),
	'16': (1,0)
}
efunc = EnergyFunction(energies)
x = ds.Lattice(20, efunc)
# print 'x.size=',x.size
#initialize with 1 cell
x.initialize(10)

print 'x.matrix=',x.matrix

# prior = Heatmap(z=x.matrix.tolist())
x.visualize()
x.runSimulation(20, 'neumann')
print 'running simulation with 20 MCS'
print 'x.matrix=',x.matrix
x.visualize(hold=True)

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
print str(x.energyFunction.determineInteractionStrength(cell1, cell3))
print str(x.energyFunction.determineInteractionStrength(cell3, cell1))
print 'this should be different'
print str(x.energyFunction.determineInteractionStrength( cell1, cell2 ))

