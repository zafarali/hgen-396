# This is an experiment to see how long simulations take
# on a 
# simulated. We can then simulate increasingl number of timesteps
# to see how long it takes

# import necessary components
from CellularPottsModel import CellularPottsModel
from EnergyFunction import EnergyFunction
from CustomEnergyFunctions import CustomEnergyFunctions

### ----- D E F A U L T   P A R A M E TE R S -----###
DEFAULT_ENERGY_FUNCTION = EnergyFunction(
	{
		'1,1':1,
		'1,0':10,
	},
	{
		'AreaConstraint' : CustomEnergyFunctions.AreaConstraint
	}
)
DEFAULT_SIMULATION_PARAMETERS = {
	'method': 'neumann',
	'showVisualization': False,
	'mutationRate':0.0
}
DEFAULT_INIT_PARAMETERS = {
	'method' : 'central',
	'starterArea': 25,
	'name': '0'
}

import sys
from timeit import repeat
import numpy as np

### ----- S I M U L A T I O N  L O O P ---- ####
def simulate( M, N, MCS ):
	DEFAULT_INIT_PARAMETERS['name'] = str(int(DEFAULT_INIT_PARAMETERS['name'])+1)
	x = CellularPottsModel( M , DEFAULT_ENERGY_FUNCTION , specialObjects = {})
	x.initialize( (M*M)/25 , **DEFAULT_INIT_PARAMETERS )
	x.runSimulation( MCS , **DEFAULT_SIMULATION_PARAMETERS )

solutions = [0 for i in range(0,40)]

### --- T I M I N G S -----####
for M in range(1,41):
	repeats = repeat('simulate('+str(M)+', '+str(M)+', 500)', setup='from __main__ import simulate', repeat=3, number=1)
	solutions[M-1] = np.mean(repeats)
print solutions
import csv
c = csv.writer ( open( 'performance2.csv', "wb" ) )
c.writerow(solutions)
