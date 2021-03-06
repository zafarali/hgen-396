from Lattice import Lattice
from Cell import Cell
from EnergyFunction import EnergyFunction
from Tools import Tools
import matplotlib.pyplot as plt
import numpy as np

"""
    Contains an implementation of the CPM and the metropolis algorithm
    which allows evolution

"""

class CellularPottsModel(Lattice):

    CELL_AREA_DEFAULT = 20

    def __init__(self, size, energyFunction, specialObjects = {}):
        Lattice.__init__(self, size, energyFunction, specialObjects)

    def deepCopy(self, name='GenericLattice2D'):
        copy = CellularPottsModel(self.size, self.energyFunction, self.specialObjects)
        copy.initialize(self.numberOfCells, name=name)
        copy.matrix = np.copy(self.matrix)
        return copy

    def metropolis(self, method='moore', showVisualization=False, mutationRate = 0):

        # checks if all cells are dead, if they are then just return ALLCELLSDEAD string
        if self.allCellsDead():
            return 'ALLCELLSDEAD'

        #executes one spin copy attempt

        #choose a lattice site at random.
        x,y=np.random.randint(self.size,size=2)
        print 'location x,y=',x,y, ',cell at this location:',self.getSpinAt(x,y)

        #get the cell and cell type

        # print 'selected x,y: ',x,y

        selected_cell = {'Cell': self.getCellAt( x, y ), \
                        'Spin': self.getSpinAt( x, y ) }


        #pick a random value of spin from the range exhibited by the neighbours

        neighbours = self.getNeighbourIndices( x, y , method )
        neighbourCells = []

        ## this for loop checks the neighbours returned to see if they are
        ## edge cases or not, if they are they are discarded
        ## if they are not, we get the CELL at that position and 
        ## append it to the neighbourCells list to be used later.
        for neighbour in neighbours:
            if not self.isEdgeCase(neighbour[0], neighbour[1]):
                neighbourCells.append( self.getCellAt( neighbour[0], neighbour[1] ) )
            else:
                neighbours.remove(neighbour)
        

        if len(neighbourCells) == 0:
            return

        
        # checks if all neighbours are 0 and you too are 0, this means that you should skip this turn
        if sum([neighbour.getType() for neighbour in neighbourCells]) == 0 and selected_cell['Cell'].getType() == 0:
            return

        # calculate H_initial
        currentCell  = selected_cell['Cell']

        
        #special options dict
        options = { 
            'x': x, 
            'y': y, 
            'neighbours': len(neighbourCells),
            'specialObjects': self.specialObjects,
            'cellList': self.cellList,
            'numberOfCells': self.numberOfCells,
            # the list comprehension below generates a list of celltarget areas
            # where the index corresponds to the spin and the value corresponds to the cell target
            'cellTargetAreaList': [ self.cellTargetAreaList[ (str(self.getCellWithSpin(i).getType())) ] for i in range(0, self.numberOfCells+1) ]
        }


        
        H_initial = self.energyFunction.calculateH( currentCell, neighbourCells, options )
        print 'H_initial=',H_initial
        print '--'
        # print 'H_initial:',H_initial
        # select a trial spin from neighbours
        randomIndex = np.random.randint(len(neighbourCells))
        trialNeighbour = neighbourCells[randomIndex]
        
        # print 'Trial spin:',trialSpin
        options['x'] = neighbours[randomIndex][0]
        options['y'] = neighbours[randomIndex][1]

        ## increasing and decreasing respective areas
        ## to be able to calcualte the contribution from the area constraint term
        currentCell.decreaseArea()
        trialNeighbour.increaseArea()

        # calculate H_final
        H_final = 0
        H_final = self.energyFunction.calculateH( trialNeighbour, neighbourCells, options )
        print 'H_final=',H_final

        ## reverting the areas back to the original
        currentCell.increaseArea()
        trialNeighbour.decreaseArea()

        # print 'H_final',H_final

        # deltaH = H_final - H_initial
        deltaH = H_final - H_initial
        print 'deltaH=',deltaH
        # print 'deltaH',deltaH
        #change the spin using special probability function. 
        spinTrue = np.random.binomial(1, Tools.boltzmannProbability( deltaH, self.DEFAULT_TEMPERATURE ) )
        # print 'spinTrue:',spinTrue

        if spinTrue:
            self.setLatticePosition(x,y, trialNeighbour.getSpin() ,True)
            if showVisualization:
                self.visualize()
        print 'change spin?', bool(spinTrue)
        selected_cell['Cell'].evolve( mutationRate = mutationRate )

    
    def runSimulation(self, MCS, method='moore', showVisualization=False, **kwargs):
        # 1 Monte Carlo Time Step = N Spin copy attempts
        mutationRate = kwargs.get('mutationRate' , 0)
        # lastSave = 0
        for i in range(0, MCS * self.size):
            thisMCS = int ( i / float(self.size) ) 
            # if thisMCS % 1000 == 0 and thisMCS != lastSave:
            #     lastSave = thisMCS
            #     filename = self.name + '_' + str( thisMCS ) + 'MCS'
            #     self.saveData(filename=filename)
            print '--------',i,'th Spin Copy Attempt / ', thisMCS , 'th MCS --------'
            if self.metropolis(method=method, showVisualization=showVisualization, mutationRate=mutationRate) is 'ALLCELLSDEAD': break
