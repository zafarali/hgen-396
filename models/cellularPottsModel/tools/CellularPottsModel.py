from Lattice import Lattice
from Cell import Cell
from EnergyFunction import EnergyFunction
from Tools import Tools
import matplotlib.pyplot as plt
import numpy as np

class CellularPottsModel(Lattice):

    CELL_AREA_DEFAULT = 40

    def __init__(self, size, energyFunction, specialObjects = {}):
        Lattice.__init__(self, size, energyFunction, specialObjects)

    # def initialize(self, numberOfCells, cellTargetAreaList={'0': -1, '1': CELL_AREA_DEFAULT, '2': CELL_AREA_DEFAULT}):
    #     # number of cells must now be a square number
    #     self.numberOfCells = numberOfCells
    #     self.cellTargetAreaList = cellTargetAreaList       
    #     self.cellList = [Cell(1, i-1) for i in range(1,numberOfCells+2)]
    #     self.cellList[0] = Cell(0)

    #     s = 20  # average cell size
    #     side = Tools.sqrt( numberOfCells * s )
    #     center = ( self.size/2.0, self.size/2.0 )
    #     top = ( round(center[0] - side/2.0),  round(center[1] - side/2.0) )

    #     cellNumber = 1
    #     cycle = 1


    #     index = [ int ( top[0] ) , int ( top[1] ) ]

    #     while ( cellNumber < numberOfCells ):
    #         if ( index[1] > int(top[1]) + int(side) ):
    #             # reset the x index, increement the y index by 1
    #             index[1] = int ( top[1]  )
    #             index[0] = int ( top[0] + 1 )

    #         self.setLatticePosition( index[1], index[0] , cellNumber )
    #         self.setLatticePosition( index[1]+1, index[0] , cellNumber )
    #         self.setLatticePosition( index[1]+2, index[0] , cellNumber )

    #         #increment the x index
    #         index[0] = index[0] + 1

    #         # deal with cycles
    #         cycle = cycle + 2
    #         if cycle > s:
    #             cycle = 1
    #             cellNumber = cellNumber + 1


    #     #HOPE THIS WORKS??
    #     self.imageRep = plt.imshow(self.matrix, interpolation='nearest')
    #     plt.colorbar(orientation='vertical')
    #     plt.draw()

    def metropolis(self, method='moore', showVisualization=False):

        if self.allCellsDead():
            return 'ALLCELLSDEAD'

        #executes one spin copy attempt

        #choose a lattice site at random.
        x,y=np.random.randint(self.size,size=2)
        #x = Tools.rndm(0, self.size-1)
        #y = Tools.rndm(0, self.size-1)

        #get the cell and cell type

        selected_cell = {}
        
        # while not self.isPositionOccupied( x, y ):
        #     x = Tools.rndm(0, self.size-1)
        #     y = Tools.rndm(0, self.size-1)

        # print 'selected x,y: ',x,y

        selected_cell = {'Cell': self.getCellAt( x, y ), \
                        'Spin': self.getSpinAt( x, y ) }


        #pick a random value of spin from the range exhibited by the neighbours

        neighbours = self.getNeighbourIndices( x, y , method)
        neighbourCells = []

        for neighbour in neighbours:
            # we first make sure we are not over reaching the board
            if not self.isEdgeCase(neighbour[0], neighbour[1]):
                neighbourCells.append( self.getCellAt( neighbour[0], neighbour[1] ) )
            else:
                neighbours.remove(neighbour)
        # print '#neighbours:',len(neighbourCells)
        
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
        # print 'H_initial:',H_initial
        # select a trial spin from neighbours
        randomIndex = Tools.rndm( 0, len(neighbourCells)-1 )
        trialNeighbour = neighbourCells[randomIndex]
        
        # print 'Trial spin:',trialSpin
        print 'x_initial=',options['x']
        options['x'] = neighbours[randomIndex][0]
        options['y'] = neighbours[randomIndex][1]
        print 'x_trial=',options['x']
        # calculate H_final
        H_final = 0
        H_final = self.energyFunction.calculateH( trialNeighbour, neighbourCells, options )
        print 'H_final=',H_final
        # print 'H_final',H_final

        # deltaH = H_final - H_initial
        deltaH = H_final - H_initial
        print 'deltaH=',deltaH
        # print 'deltaH',deltaH
        #change the spin using special probability function. 
        spinTrue = Tools.probability( Tools.boltzmannProbability( deltaH, self.DEFAULT_TEMPERATURE ) )
        # print 'spinTrue:',spinTrue

        if spinTrue:
            self.setLatticePosition(x,y, trialNeighbour.getSpin() ,True)
            if showVisualization:
                self.visualize()
        print spinTrue
        selected_cell['Cell'].evolve()

    
    def runSimulation(self, MCS, method='moore', showVisualization=False):
        # 1 Monte Carlo Time Step = N Spin copy attempts
        for i in range(0, MCS * self.size):
            if self.metropolis(method=method, showVisualization=showVisualization) is 'ALLCELLSDEAD': break
