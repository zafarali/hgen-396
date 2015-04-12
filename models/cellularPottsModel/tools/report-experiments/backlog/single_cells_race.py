__author__ = 'zafarali'

# Experiment: Race between 4 single cells.

# import necessary components
from CellularPottsModel import CellularPottsModel
from EnergyFunction import EnergyFunction
from CustomEnergyFunctions import CustomEnergyFunctions
from Gradient import Gradient


e_func = EnergyFunction(
	{ #surface energies
		'1,1':1,
		'1,0':10
	},
	{ # custom energy functions
		'AreaConstraint' : CustomEnergyFunctions.AreaConstraint,
		'Y-gradient' : CustomEnergyFunctions.yGradientInteract
	}
)

# gradient for the races
gradients = {
	'Y-gradient': Gradient( lambda x: 26 * x, 49, interactionStrength = 20 )
}

# a M=49 lattice is created
x = CellularPottsModel( 49 , e_func , specialObjects = gradients )

# starting positions and areas for the single cell race
initializationParameters = {
	'method' : 'custom',
	'pos':[(5,5), (5,15), (5, 25), (5,35)],
	'starterArea': 20,
	'name': 'Single Cell Race'
}
# initialize the lattice with the cells
x.initialize( 4 , **initializationParameters )
# save the state of the lattice before the race is run

x.saveData('single_cells_race_before')

# Run the race, set the mutation rate to 0 to avoid problems with type 2 cells
simulationParameters = {
	'method': 'neumann',
	'showVisualization': False,
	'mutationRate':0.00
}

x.runSimulation( 8000 , **simulationParameters )

# save the data after the race completed
x.saveData('single_cells_race_after')

print 'Simulation Complete'
