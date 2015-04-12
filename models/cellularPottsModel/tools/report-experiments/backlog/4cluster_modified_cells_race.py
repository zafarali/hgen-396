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
	'Y-gradient': Gradient( lambda x: 26 * x, 64, interactionStrength = 20 )
}

x = CellularPottsModel( 64 , e_func , specialObjects = gradients )

initializationParameters = {
	'method' : 'custom',
	'pos':[
		(2,12),(6,10),(6,14),(10,12), \
		(6,25), (6,29), (2,27), (10, 27), \
		(6, 38), (6, 42), (2, 40), (10, 40), \
		(6, 50), (6, 54), (2, 52), (10, 52)\
	 ],
	'starterArea': 20,
	'name': 'Race'
}
x.initialize( len(initializationParameters['pos']) , **initializationParameters )

# x.saveData('4cluster_diamon_before')
simulationParameters = {
	'method': 'neumann',
	'showVisualization': False,
	'mutationRate':0.00
}

# save for before and after comparison
x.runSimulation( 8000 , **simulationParameters )

x.saveData('4cluster_diamon_after')
print 'Simulation Complete'

# x.visualize(hold=True)

