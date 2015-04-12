# Experiment to run k-CTCs

# import necessary components
from CellularPottsModel import CellularPottsModel
from EnergyFunction import EnergyFunction
from CustomEnergyFunctions import CustomEnergyFunctions
from Gradient import Gradient
#### ---- D E F A U L T   P A R A M E T E R S ---- ####
DEFAULT_ENERGY_FUNCTION = EnergyFunction(
	{
		'1,1':1,
		'1,0':5,
	},
	{
		'AreaConstraint' : CustomEnergyFunctions.AreaConstraint,
		'Y-gradient' : CustomEnergyFunctions.yGradientInteract,
	}
)
DEFAULT_SIMULATION_PARAMETERS = {
	'method': 'neumann',
	'showVisualization': False,
	'mutationRate':0.0
}
DEFAULT_INIT_PARAMETERS = {
	'method' : 'custom',
	'starterArea': 20,
	'pos':[(5,30),(5,34)],
	'name': '0'
}
gradients = {
	'Y-gradient': Gradient( lambda x: 26 * x, 100, interactionStrength = 20 )
}

STARTING_POSITIONS = [
	[ ( 5, 45 ) ],
	[ ( 5, 30 ), ( 5, 34 ) ],
	[ ( 5, 30 ), ( 5, 34 ), ( 9, 32 ) ],
	[ ( 5, 30 ), ( 5, 34 ), ( 9, 30 ), ( 9, 34 ) ],
	[ ( 5, 30 ), ( 5, 34 ), ( 9, 30 ), ( 9, 34 ), ( 13, 32 ) ],
	[ ( 5, 25 ), ( 5, 29 ), ( 5, 33 ), ( 9, 25 ), ( 9, 29 ), ( 9, 33 ) ],
	[ ( 5, 30 ), ( 5, 34 ), ( 7, 26 ), ( 9, 30 ), ( 9, 34 ), ( 7, 38 ), ( 13, 32 ) ],
	[ ( 5, 32 ), ( 9, 30 ), ( 9, 34 ), ( 11, 26 ), ( 11, 38 ), ( 13, 30 ), ( 13, 34), ( 17, 32 ) ],
	[ ( 5, 26 ), ( 5, 30 ), ( 5, 34 ), ( 9, 26 ), ( 9, 30 ), ( 9, 34 ), ( 13, 26 ), ( 13, 30 ), ( 13, 34 ) ],
	[ ( 10, 24 ), ( 9, 28 ), ( 9, 32 ), ( 9, 36 ), ( 10, 40 ), ( 5, 32 ), ( 13, 28 ), ( 13, 32 ), ( 17, 32 ), ( 13, 36 )]
]	

import numpy as np
import matplotlib.pyplot as plt

def simulate(N, i):
	DEFAULT_INIT_PARAMETERS['name'] = './experiments/'+str(N)+'_'+str(i)

	x = CellularPottsModel( 100 , DEFAULT_ENERGY_FUNCTION , specialObjects = gradients )
	x.initialize( len(DEFAULT_INIT_PARAMETERS['pos']) , **DEFAULT_INIT_PARAMETERS )
	x.runSimulation( 10000 , **DEFAULT_SIMULATION_PARAMETERS)
	x.saveData('./experiments/'+str(N)+'_'+str(i))
	# x.visualize(hold=True)

for N in range(0, len(STARTING_POSITIONS)+1):
	# SET THE STARTING POSITONS	
	DEFAULT_INIT_PARAMETERS['pos'] = STARTING_POSITIONS[N-1]

	# SAVE PRIOR DATA
	q = CellularPottsModel( 100, DEFAULT_ENERGY_FUNCTION, specialObjects = gradients )
	q.initialize ( len(DEFAULT_INIT_PARAMETERS['pos']) , **DEFAULT_INIT_PARAMETERS )
	q.saveData( './experiments/BEFORE_' + str(N) )
	del q
	for i in range(0,10):
		# RUN SIMULATIONS
		simulate(N, i)
