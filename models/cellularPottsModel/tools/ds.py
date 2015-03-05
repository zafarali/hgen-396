__author__ = 'zafarali'
__version__ = '0.0.1'
# Datastructure to help facillitate cellular potts

import numpy as np
import matplotlib.pyplot as plt
from Cell import Cell
from Tools import Tools

class Lattice:
    # constants
    DIMENSION = 2
    CELL_AREA_DEFAULT = 9
    DEFAULT_TEMPERATURE = 5

    # attributes
    size = 0
    name = 'GenericLattice2D'
    
    
    # size = size of lattice
    # energyFunction associated with this lattice
    # specialObjects are special locations on the lattice which are occupied with objects

    def __init__(self, size, energyFunction, specialObjects = {}):
        self.size = size
        #create the matrix of zeros (essentially a blank lattice
        self.energyFunction = energyFunction
        self.matrix = np.zeros((size,size))
        self.specialObjects = specialObjects

    def isEdgeCase(self, x,y):
        return Tools.isEdgeCase(x,y,0,self.size-1)

    def deepCopy(self):
        copy = Lattice(self.size)
        copy.initialize(self.numberOfCells, self.cellArea)
        copy.matrix = np.copy(self.matrix)
        return copy

    def giveName(self, name):
        self.name = name
    def initialize(self, numberOfCells, cellArea=CELL_AREA_DEFAULT):
        self.cellArea = cellArea
        self.numberOfCells = numberOfCells
        
        # code to initialize cell list
        self.cellList = [Cell(1, i-1) for i in range(1,numberOfCells+2)]
        self.cellList[0] = Cell(0)
        
        #code to initialize lattice here
        cycle = 1
        # we start from the middle of the lattice
        cellIndex = [self.size/2, self.size/2]
        for i in range(1,numberOfCells+1):
            if(self.setLatticePosition(cellIndex[0], cellIndex[1], i)):
                # set everything the the von neumann neighbourhood
                # to the same cell type
                self.setLatticePosition(cellIndex[0],cellIndex[1]-1,i)
                self.setLatticePosition(cellIndex[0],cellIndex[1]+1,i)
                self.setLatticePosition(cellIndex[0]-1,cellIndex[1],i) 
                self.setLatticePosition(cellIndex[0]-1,cellIndex[1],i)
                #update one lattice site outside the von neumann neighbourhood to be the same as the current cell
                switch = Tools.rndm(1,4)
                if switch == 1:
                    self.setLatticePosition(cellIndex[0]+1,cellIndex[1]+1,i)
                elif switch == 2:
                    self.setLatticePosition(cellIndex[0]+1,cellIndex[1]-1,i)
                elif switch == 2:
                    self.setLatticePosition(cellIndex[0]-1,cellIndex[1]+1,i)
                else:             
                    self.setLatticePosition(cellIndex[0]-1,cellIndex[1]-1,i)
            else:
                i -= 1
            # update coordinates for next location
            # print i
            
            switch = i%4
            
            if switch == 1:
                cellIndex[1] = cellIndex[1] - (cycle * 2)
            elif switch == 2:
                cellIndex[0] = cellIndex[0] + (cycle * 2)
            elif switch == 3:
                cellIndex[1] = cellIndex[1] + (cycle * 2)
            else:
                cycle += 1
                cellIndex[1] +=1
                cellIndex[0] = cellIndex[0] - (cycle*2)
        
        # for visualizing the matrix 
        self.imageRep = plt.imshow(self.matrix, interpolation='nearest')
        plt.colorbar(orientation='vertical')
        plt.draw()


    def isPositionOccupied(self, x, y):
        return bool(self.matrix[x][y])
    def setLatticePosition(self, x, y, value, override=False):
        # Sets a lattice position (x,y) to value = value
        # returns true if position was not occupied and it was updated
        # returns false if the position was occupied and it was not updated
        # override is a boolean that allows us to update even though position is occupied
        # print x,y,self.size

        if x < self.size and y < self.size:
            if (override == True) or (not self.isPositionOccupied(x,y)):
                self.matrix[x][y] = value
                if isinstance(value, np.float64):
                    value = value.astype(int)
                self.cellList[value].increaseArea()
                return True
            else:
                return False
    def getNeighbourIndices(self, x, y, method='moore'):
        # returns the moore neighbourhood around x and y
        # WARN: this doesn't check for edge cases...
        if method is 'neumann':
            return [[x, y-1], [x, y+1], [x+1, y], [x-1, y]]
        else:
            return [[x, y+1], [x+1, y], [x,y-1], [x-1,y], [x+1,y+1], [x-1,y+1], [x-1, y-1], [x+1,y-1]]

    def getCellAt(self, x, y):
        #returns the cell occupying lattice position x,y
        x = int(x)
        y = int(y)        
        return self.cellList[self.matrix[x][y].astype(int)]

    def getCellWithSpin(self, spin):
        #returns the cell with spin = spin

        return self.cellList[spin.astype(int)]

    def getSpinAt(self, x, y):
        x = int(x)
        y = int(y)
        return self.matrix[x][y]

    def metropolis(self, method='moore', showVisualization=False):
        #executes one spin copy attempt

        #choose a lattice site at random.
        x = Tools.rndm(0, self.size-1)
        y = Tools.rndm(0, self.size-1)

        #get the cell and cell type

        selected_cell = {}
        
        # while not self.isPositionOccupied( x, y ):
        #     x = Tools.rndm(0, self.size-1)
        #     y = Tools.rndm(0, self.size-1)

        # print 'selected x,y: ',x,y

        selected_cell = {'Cell': self.getCellAt(x, y), \
                        'Spin': self.getSpinAt( x, y ) }


        #pick a random value of spin from the range exhibited by the neighbours

        neighbours = self.getNeighbourIndices( x, y , method)
        neighbourCells = []

        for neighbour in neighbours:
            # we first make sure we are not over reaching the board
            if not self.isEdgeCase(neighbour[0], neighbour[1]):
                # now we check that we haven't selected a extra cellular position
                if self.getSpinAt(neighbour[0], neighbour[1]).astype(int) != 0:
                    neighbourCells.append( self.getCellAt( neighbour[0], neighbour[1] ) )
        
        # print '#neighbours:',len(neighbourCells)
        
        if len(neighbourCells) == 0:
            return

        # calculate H_initial
        currentCell  = selected_cell['Cell']


        #special options dict
        options = { 
            'x': x, 
            'y': y, 
            'neighbours': len(neighbourCells),
            'specialObjects': self.specialObjects 
        }

        H_initial = 0
        for neighbourCell in neighbourCells:
            H_initial += self.energyFunction.calculateH( currentCell, neighbourCell, options )

        # print 'H_initial:',H_initial
        # select a trial spin from neighbours
        trialNeighbour = neighbourCells[ Tools.rndm( 0, len(neighbourCells)-1 ) ]
        
        # print 'Trial spin:',trialSpin
        # calculate H_final
        H_final = 0
        for neighbourCell in neighbourCells:
            H_final = H_final + self.energyFunction.calculateH( trialNeighbour, neighbourCell )

        # print 'H_final',H_final

        # deltaH = H_final - H_initial
        deltaH = H_final - H_initial
        # print 'deltaH',deltaH
        #change the spin using special probability function. 
        spinTrue = Tools.probability( Tools.boltzmannProbability( deltaH, self.DEFAULT_TEMPERATURE ) )
        # print 'spinTrue:',spinTrue

        if spinTrue:
            self.setLatticePosition(x,y, trialNeighbour.getSpin() ,True)
            if showVisualization:
                self.visualize()

        selected_cell['Cell'].evolve()

    
    def runSimulation(self, MCS, method='moore', showVisualization=False):
        # 1 Monte Carlo Time Step = N Spin copy attempts
        for i in range(0, MCS * self.size):
            self.metropolis(method=method, showVisualization=showVisualization)

    #### TRYING TO VISUALIZE THE CELL TYPES ####
    def getCellTypeForSpin(self,x):
        x = int(x)
        cell = self.getCellWithSpin(x)
        return cell.getType()

    def visualize(self, hold=False):
        self.imageRep.set_data(self.matrix)
        if not hold:
            plt.draw()
            plt.pause(0.01)
        else:
            plt.show()

        