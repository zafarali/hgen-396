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
    CELL_AREA_DEFAULT = 20
    DEFAULT_TEMPERATURE = 100

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

    def allCellsDead(self):
        cellsDead = [cell.isDead() for cell in self.cellList]
        # print cellsDead
        # returns true if all values in cellAlive are 1.
        return sum(cellsDead) >= self.numberOfCells 

    def initialize(self, numberOfCells, cellTargetAreaList={'0': -1, '1': CELL_AREA_DEFAULT, '2': CELL_AREA_DEFAULT}):
        self.cellTargetAreaList = cellTargetAreaList
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
                switch = np.random.random_integers(1,4)
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
            oldValue = self.matrix[x][y]
            if (override == True) or (not self.isPositionOccupied(x,y)):
                self.matrix[x][y] = value
                if isinstance(value, np.float64):
                    value = value.astype(int)

                oldValue = oldValue.astype(int)
                self.cellList[value].increaseArea()
                self.cellList[oldValue].decreaseArea()
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
        return self.cellList[spin.astype(int) if isinstance(spin, np.float64) else spin]

    def getSpinAt(self, x, y):
        x = int(x)
        y = int(y)
        return self.matrix[x][y]

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

        