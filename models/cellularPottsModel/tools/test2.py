from CellularPottsModel import CellularPottsModel
from EnergyFunction import EnergyFunction
energies = {
	'1': (1,1),
	'4': (1,2),
	'8': (2,2),
	'10': (2,0),
	'10': (1,0)
}
efunc = EnergyFunction(energies)

# initialize a M x M lattice (M = 20)
x = CellularPottsModel(25, efunc)

# initialize with N=10 cells using the central method
x.initialize(16, method='central', starterArea=10)
# x.runSimulation(100, 'neumann', showVisualization=True)
x.visualize(hold=True)
