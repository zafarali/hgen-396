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
	'pos':[(5,5), (5,9), (5, 20), (5,35), (5,24), (5,39), (5, 50), (5,54), (9,5), (9,9), (9,20), (9,24), (9,35), (9,50), (9,39), (9,54)],
	'starterArea': 20,
	'name': 'Race'
}
x.initialize( 16 , **initializationParameters )

simulationParameters = {
	'method': 'neumann',
	'showVisualization': False,
	'mutationRate':0.00
}

# save for before and after comparison
x.runSimulation( 8000 , **simulationParameters )

x.saveData('4cluster_race_after')
print 'Simulation Complete'

x.visualize(hold=True)

