__author__ = 'zafarali'
#To change this template use Tools | Templates.
#
#

## plotting stuff
# import plotly.plotly as pltly
# from plotly.graph_objs import *
# import plotly.tools as pltls

from CellularPottsModel import CellularPottsModel
from EnergyFunction import EnergyFunction
from Cell import Cell
from CustomEnergyFunctions import CustomEnergyFunctions
from Gradient import Gradient

energies = {
	'5': (1,1),
	'0': (1,2),
	'0': (2,2),
	'0': (2,0),
	'16': (1,0)
}

specialFunctions = {
	'OxygenGradientInteract': CustomEnergyFunctions.OxygenGradientInteract,
	'AreaConstraint': CustomEnergyFunctions.AreaConstraint
}

import numpy as np
gradients = {
	'OxygenGradient': Gradient(lambda x: (x-30)**2 , 30, interactionStrength=200000000000),
}
gradients2 = {
	'OxygenGradient': Gradient(lambda x: -(x-30)**2 , 30, interactionStrength=1500000),
}
efunc = EnergyFunction(energies, specialFunctions)

x = CellularPottsModel(30, efunc, specialObjects=gradients)
# y = CellularPottsModel(30, efunc, specialObjects=gradients2)
x.initialize(20, method='central', starterArea=20)
# y.initialize(20, method='central', starterArea=20)

x.saveData('positive-x-squared-pre')
# y.saveData('negative-x-squared-pre')

# lattici = []
# for i in range(0, 2):
	# lattici.append(x.deepCopy())

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


# print 'x.matrix=',x.matrix

# prior = Heatmap(z=x.matrix.tolist())
# print 'running 50 lattices'
# print 'running simulation with 100 MCS (neumann neighbourhood function)'

# for index,lattice in enumerate(lattici):
	# lattice.runSimulation(20, method='neumann', showVisualization=True)
	# lattice.saveData('gradientExperiment-'+str(index), what='cells')
	# data.append([ cell.getArea() for cell in lattice.cellList if cell.getArea() > -1])

x.runSimulation(1000, method='neumann', showVisualization=False)
# y.runSimulation(400, method='neumann', showVisualization=False)
print x.allCellsDead()
print 'simulations over'

x.saveData('positive-x-squared-post')
# y.saveData('negative-x-squared-post')

fig1 = plt.figure(2)
plt.plot(x.specialObjects['OxygenGradient'].interactions)
plt.title('positive-x-squared')
plt.xlabel('position')
plt.ylabel('magnitude')

# fig2 = plt.figure(3)
# plt.plot(y.specialObjects['OxygenGradient'].interactions)
# plt.title('negative-x-squared')
# plt.xlabel('position')
# plt.ylabel('magnitude')
plt.show()



