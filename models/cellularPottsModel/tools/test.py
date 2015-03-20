__author__ = 'zafarali'
#To change this template use Tools | Templates.
#
#

## plotting stuff
# import plotly.plotly as pltly
# from plotly.graph_objs import *
# import plotly.tools as pltls

from CellularPottsModel import CellularPottsModel
from EnergyFunction import EnergyFunction
from Cell import Cell
from CustomEnergyFunctions import CustomEnergyFunctions
from Gradient import Gradient

energies = {
	'1': (1,1),
	'4': (1,2),
	'8': (2,2),
	'10': (2,0),
	'10': (1,0)
}

specialFunctions = {
	'AreaConstraint': CustomEnergyFunctions.AreaConstraint,
	'OxygenGradientInteract': CustomEnergyFunctions.OxygenGradientInteract,	
	'NutrientInteract': CustomEnergyFunctions.NutrientInteract
}
specialObjects = {
	'OxygenGradient': Gradient(lambda x: -x , 20, interactionStrength=500),
	'NutrientGradient': Gradient(lambda x: -x + 20, 20, interactionStrength=1000)
}
efunc = EnergyFunction(energies, specialFunctions)

x = CellularPottsModel(20, efunc, specialObjects=specialObjects)
# print 'x.size=',x.size
#initialize with 1 cell
x.initialize(10)

# print 'x.matrix=',x.matrix

# prior = Heatmap(z=x.matrix.tolist())
x.visualize()
print 'running simulation with 100 MCS (neumann neighbourhood function)'
x.runSimulation(100, 'neumann', showVisualization=True)
print 'simulation over'
print x.cellList
# print 'x.matrix=',x.matrix
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
cell1 = Cell(1)
cell2 = Cell(1)
cell3 = Cell(2)


print 'the following should print the same thing on two lines:'
print str(x.energyFunction.determineInteractionStrength(cell1, cell3))
print str(x.energyFunction.determineInteractionStrength(cell3, cell1))
print 'this should be different'
print str(x.energyFunction.determineInteractionStrength( cell1, cell2 ))

