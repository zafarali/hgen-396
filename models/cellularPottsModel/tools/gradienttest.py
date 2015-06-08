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
	'1,1':1,
	'1,2':0,
	'2,2':0,
	'2,0':0,
	'1,0':5
}

specialFunctions = {
	'X-gradient': CustomEnergyFunctions.xGradientInteract,
	'AreaConstraint': CustomEnergyFunctions.AreaConstraint
}

import numpy as np
gradients = {
	'X-gradient': Gradient(lambda x: (27*x)**1 , 9, interactionStrength=1),
}
gradients2 = {
	'X-gradient': Gradient(lambda x: 0 , 9, interactionStrength=1),
}
efunc = EnergyFunction(energies, specialFunctions)

x = CellularPottsModel(100, efunc, specialObjects=gradients)
y = CellularPottsModel(100, efunc, specialObjects=gradients2)
x.initialize(90, method='central', starterArea=1, name='c = +27')
y.initialize(90, method='central', starterArea=1, name='control')

x.saveData('testc-x')
y.saveData('testc-control')

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


x.runSimulation(10000, method='neumann', showVisualization=False)
y.runSimulation(10000, method='neumann', showVisualization=False)

print 'simulations over'

x.visualize()
y.visualize()

fig1 = plt.figure('c+30 test')
plt.plot(x.specialObjects['X-gradient'].interactions)
plt.title('c = +30 test')
plt.xlabel('position')
plt.ylabel('magnitude')

fig2 = plt.figure('c control')
plt.plot(y.specialObjects['X-gradient'].interactions)
plt.title('control')
plt.xlabel('position')
plt.ylabel('magnitude')
plt.show()



