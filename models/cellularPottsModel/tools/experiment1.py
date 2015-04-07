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
		'1,0':5,
		'2,0':-5,
		'2,2':1,
		'2,1':100
	},
	{
		'AreaConstraint' : CustomEnergyFunctions.AreaConstraint,
		'Y-gradient' : CustomEnergyFunctions.yGradientInteract,
		'X-gradient': CustomEnergyFunctions.xGradientInteract
	}
)

gradients = {
	'X-gradient': Gradient( lambda x: 27 * x if x > 25 else -27 * x , 100 , interactionStrength = 1 ),
	'Y-gradient': Gradient( lambda x: 30 * x if (x > 40 and x < 60) else 0, 100, interactionStrength = 1000 )
}

x = CellularPottsModel( 100 , e_func , specialObjects = gradients )
# initialize with 20 cells 
initializationParameters = {
	'method' : 'central',
	'starterArea': 25,
	'name': 'Experiment 9terminal'
}
x.initialize( 150 , **initializationParameters )
simulationParameters = {
	'method': 'neumann',
	'showVisualization': False,
	'mutationRate':0.01
}
x.runSimulation( 1000 , **simulationParameters )

print 'Simulation Complete'
print '-------CELLS------'
cell_info = [ ( cell.getSpin() , cell.getType() == 2 , cell.isDead(), cell.getArea() ) for cell in x.cellList ]
print cell_info


x.visualize()
import matplotlib.pyplot as plt
try:
	fig1 = plt.figure('x-gradient')
	plt.plot(x.specialObjects['X-gradient'].interactions)
	plt.title('x-gradient visualization')
	plt.xlabel('position')
	plt.ylabel('magnitude')

	fig2 = plt.figure('y-gradient')
	plt.plot(x.specialObjects['Y-gradient'].interactions)
	plt.title('y-gradient visualization')
	plt.xlabel('position')
	plt.ylabel('magnitude')

	plt.show()
except Exception:
	print 'Failed to print gradient graph'




# give option to save the input
saveInput = raw_input('save input? (y/n):')
if saveInput is 'y':
	# saveWhat = raw_input('save what? (all *default*, cells, lattice) ')
	saveWhat = 'all'
	if not ( saveWhat == 'lattice' or saveWhat == 'all' or saveWhat == 'cells' ) : 
		print 'input:',saveWhat,'not a keyword argument, defaulting to all'
		saveWhat = 'all'
	fileName = raw_input('fileName?')
	print saveWhat, fileName
	x.saveData(what=saveWhat, filename=fileName)
