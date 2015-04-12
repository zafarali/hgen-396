__author__ = 'zafarali'

# Experiment: Single 1D gradient on a group of cells

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
		'2,0':10,
		'2,2':1,
		'2,1':10
	},
	{
		'AreaConstraint' : CustomEnergyFunctions.AreaConstraint,
		'Y-gradient' : CustomEnergyFunctions.yGradientInteract,
		# 'X-gradient': CustomEnergyFunctions.xGradientInteract
	}
)

gradients = {
	'Y-gradient': Gradient( lambda x: 26 * x, 49, interactionStrength = 20 )
}

x = CellularPottsModel( 64 , e_func , specialObjects = gradients )

initializationParameters = {
	'method' : 'custom',
	'pos': [
		(5, 7), (17, 7), (9, 5), (13,5), (9,9), (13, 9), \
		# (5, 25), (13, 23), (13, 27), (17, 25), (9, 23), (9, 27), \
		# (9, 37), (9, 41), (13, 37), (13, 41), (17, 39), (5, 39),\
		(9, 51), (9, 55), (13, 51), (13, 55), (17, 53), (5, 53)
	],
	'starterArea': 20,
	'name': 'Race'
}
x.initialize( len(initializationParameters['pos']) , **initializationParameters )

simulationParameters = {
	'method': 'neumann',
	'showVisualization': False,
	'mutationRate':0.00
}

# x.saveData('6cluster_race_before')
# save for before and after comparison
x.runSimulation( 8000 , **simulationParameters )

x.saveData('6cluster_race_after')
print 'Simulation Complete'


