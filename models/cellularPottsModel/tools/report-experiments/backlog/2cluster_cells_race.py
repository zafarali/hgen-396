__author__ = 'zafarali'

# Experiment: Race between 3 2-clusters of cells.

# import necessary components
from CellularPottsModel import CellularPottsModel
from EnergyFunction import EnergyFunction
from CustomEnergyFunctions import CustomEnergyFunctions
from Gradient import Gradient


# create an energy function
e_func = EnergyFunction(
	{
		'1,1':1,
		'1,0':10,
	},
	{
		'AreaConstraint' : CustomEnergyFunctions.AreaConstraint,
		'Y-gradient' : CustomEnergyFunctions.yGradientInteract,
	}
)

# gradient for the races
gradients = {
	'Y-gradient': Gradient( lambda x: 26 * x, 49, interactionStrength = 20 )
}

x = CellularPottsModel( 49 , e_func , specialObjects = gradients )

initializationParameters = {
	'method' : 'custom',
	'pos':[(5,5), (5,9), (5, 20), (5,24), (5,35), (5,39)],
	'starterArea': 20,
	'name': 'Race'
}
x.initialize( 6 , **initializationParameters )

#save the starting positions before the race starts
x.saveData('2cluster_cells_race_before')

simulationParameters = {
	'method': 'neumann',
	'showVisualization': False,
	'mutationRate':0.00
}
x.runSimulation( 8000 , **simulationParameters )

# save the data after the race has completed
x.saveData('2cluster_race_after')
print 'Simulation Complete'


