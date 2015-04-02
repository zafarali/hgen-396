__author__ = 'zafarali'

# unit tests for Cellular Potts Model

from CellularPottsModel import CellularPottsModel
from EnergyFunction import EnergyFunction
from Cell import Cell
from CustomEnergyFunctions import CustomEnergyFunctions
from Gradient import Gradient


# create the energy function
energies = {
	'1,1': 5,
	'1,2':0,
	'2,2':0,
	'2,0':0,
	'1,0':16
}
efunc = EnergyFunction(energies)

M = 9
N = 1

# create the model
x = CellularPottsModel(M, efunc)
x.initialize(N, starterArea=20, method='central')

# checking matrix creation
assert len(x.matrix) == M, 'Matrix has incorrect y dimensions'
assert len(x.matrix[1]) == M, 'Matrix has incorrect x dimensions'

# checking initialization algorithm
assert len(x.cellList) == N+1, 'Cell List is not as long as the number of cells specificed'
assert x.cellList[0].getType() == 0, 'Cell 0 is not of type: 0'
assert x.cellList[0].getSpin() == 0, 'Cell 0 is not of spin: 0'

# checking special tools
assert not x.isEdgeCase(M/2,M/2), '(M/2,M/2) was classified as an edge case'
assert x.isEdgeCase(M,M+1), '(M,M+1) was not classified as an edge case'

# testing cells
c1, c2, c3 = Cell(1), Cell(1), Cell(0)
assert c3.getType() != c2.getType, 'C3 and C2 were classified as the same type'

# testing energy function
assert efunc.pairWiseEnergy(c1, c2) == efunc.pairWiseEnergy(c2, c1), 'c1 and c2 must have the same energy interaction'
assert efunc.pairWiseEnergy(c3, c1) != efunc.pairWiseEnergy(c1, c2), 'c3 and c1 classied as the same energy as c1, c2'
assert efunc.pairWiseEnergy(c3, c3) == 0, 'ECM was classied with a non-zero energy'

# checking deepcopy function
y = x.deepCopy()
assert x.matrix.tolist() == y.matrix.tolist(), 'x and x.deepCopy() do not have the same matrix'
assert x.cellList == y.cellList, 'x and x.deepCopy() do not have the same cellList'
assert x.energyFunction.energies == y.energyFunction.energies, 'x and y do not have the same energies'
assert len(x.specialObjects) == len(y.specialObjects), 'x and y do not have the same list of special objects'

print 'Passed All Tests'