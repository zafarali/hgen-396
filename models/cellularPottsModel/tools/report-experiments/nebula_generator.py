from CellularPottsModel import CellularPottsModel
from EnergyFunction import EnergyFunction
from CustomEnergyFunctions import CustomEnergyFunctions
from Gradient import Gradient

energies = {
	'1,1':1,
	'1,0':10,
}

specialFunctions = {
	'Y-gradient':CustomEnergyFunctions.yGradientInteract,
	# 'X-gradient':CustomEnergyFunctions.xGradientInteract,
	'AreaConstraint': CustomEnergyFunctions.AreaConstraint
}

gradients = {
	'Y-gradient': Gradient( lambda x : 27 * x if x > 50 else -27 * x , 100)
}

efunc = EnergyFunction(energies, specialFunctions)

x = CellularPottsModel(100, efunc, specialObjects = gradients)
x.initialize(150, method='central', starterArea=25, name='Tissue_Splitting_10000MCS_plus')

x.runSimulation(200000, method='neumann', showVisualization=False, mutationRate=0)
x.saveData('nebula-reproduction2')
