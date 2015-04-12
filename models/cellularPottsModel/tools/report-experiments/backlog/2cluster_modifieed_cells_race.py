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

x = CellularPottsModel( 64 , e_func , specialObjects = gradients )

initializationParameters = {
	'method' : 'custom',
	'pos':[(5,10), (9,10), (5, 24), (9,24), (5,38), (9,38), (5,52), (9,52)],
	'starterArea': 20,
	'name': 'Race'
}
x.initialize( 8 , **initializationParameters )

# save the starting positions before the race starts
# x.saveData('2cluster_modified_race_before')

simulationParameters = {
	'method': 'neumann',
	'showVisualization': False,
	'mutationRate':0.00
}
x.runSimulation( 8000 , **simulationParameters )

# save the data after the race has completed
x.saveData('2cluster_modified_race_after')
x.visualize(hold=True)

print 'Simulation Complete'


