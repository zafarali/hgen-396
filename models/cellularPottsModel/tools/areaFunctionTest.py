__author__ = 'zafarali'
# This script tests if the AREA Constraint is working correctly

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
	'AreaConstraint': CustomEnergyFunctions.AreaConstraint
}

efunc = EnergyFunction(energies, specialFunctions)

x = CellularPottsModel(30, efunc, specialObjects={})


x.initialize(20, method='central', starterArea=20)

lattici = []
for i in range(0, 100):
	lattici.append(x.deepCopy())

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# get the first data point
data = []
dataprior = [ cell.getArea() for cell in x.cellList if cell.getArea() > -1]


# print 'x.matrix=',x.matrix

# prior = Heatmap(z=x.matrix.tolist())
print 'running 50 lattices'
print 'running simulation with 100 MCS (neumann neighbourhood function)'

for index,lattice in enumerate(lattici):
	lattice.runSimulation(400, method='neumann', showVisualization=False)
	data.append([ cell.getArea() for cell in lattice.cellList if cell.getArea() > -1])

print 'simulation over'

fig1 = plt.figure(2)
bins = range(0,60)
plt.hist(dataprior, bins, alpha=0.5, label='Pre')
plt.hist(data, bins, alpha=0.5, label='Post')
plt.legend(loc='upper right')
plt.xlabel('Maximum Cell Area')
plt.ylabel('Number of Cells')
plt.title('Distribution of MAX Cell Areas Pre and Post Simulation in the presence of the Area Constraint')
fig1.hold()
plt.draw()
plt.show()
print 'plotted histogram'

