# Experiment to test if single cells solve
# Trivial cases

# import necessary components
from CellularPottsModel import CellularPottsModel
from EnergyFunction import EnergyFunction
from CustomEnergyFunctions import CustomEnergyFunctions

#### ---- D E F A U L T   P A R A M E T E R S ---- ####
DEFAULT_ENERGY_FUNCTION = EnergyFunction(
	{
		'1,1':1,
		'1,0':5,
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
	'starterArea': 1,
	'name': '0'
}


import numpy as np
import matplotlib.pyplot as plt
deadcount = 0
cellareas = []

def simulate():
	DEFAULT_INIT_PARAMETERS['name'] = str(int(DEFAULT_INIT_PARAMETERS['name'])+1)
	
	global deadcount
	global cellareas

	x = CellularPottsModel( 10 , DEFAULT_ENERGY_FUNCTION , specialObjects = {})
	x.initialize( 25 , **DEFAULT_INIT_PARAMETERS )
	x.runSimulation( 250 , **DEFAULT_SIMULATION_PARAMETERS )
	
	cellareas = cellareas + [cell.getArea() for cell in x.cellList if cell.getArea() > -1]
	return 1 if x.allCellsDead() else 0

for i in range(1,100):
	deadcount += simulate()


fig1 = plt.figure('Final Cell Areas')
bins = range(0,60)
plt.hist(cellareas, bins, alpha=0.5, label='Post')
plt.xlabel('Ending Cell Areas')
plt.ylabel('Frequency')
plt.title('Distribution of Final Cell Areas, T=250MCS')
fig1.hold()
fig1.show()
raw_input()
import csv
c = csv.writer ( open( 'cellAreas2.csv', "wb" ) )
c.writerow(cellareas)
