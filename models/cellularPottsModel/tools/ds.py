__author__ = 'zafarali'
# Datastructure to help facillitate cellular potts

import numpy as np

class Tools:
    @staticmethod
    def rndm( l, r ):
        return round(np.random.random())*(r-l)
    @staticmethod
    def probability( threshold ):
        if (np.random.random() <= threshold) or threshold is 1:
            return True
        else:
            return False

class Lattice:
    # constants
    DIMENSION = 2
    CELL_AREA_DEFAULT = 9


    # attributes
    size = 0
    name = 'GenericLattice2D'
    
    
    def __init__(self, size):
        self.size = size
        #create the matrix of zeros (essentially a blank lattice
        
        self.matrix = np.zeros((size,size))
    
    def giveName(self, name):
        self.name = name
    
    def initialize(self, numberOfCells, cellArea=CELL_AREA_DEFAULT):
        self.cellArea = cellArea
        self.numberOfCells = numberOfCells
        #code to initialize lattice here
        
        # we start from the middle of the lattice
        cellIndex = [self.size/2, self.size/2]
        for i in range(1,numberOfCells+1):
            pass
        
    def isPositionOccupied(self, x, y):
        return bool(self.matrix[x][y])

    
    def setLatticePosition(self, x, y, value, override):
        # Sets a lattice position (x,y) to value = value
        # returns true if position was not occupied and it was updated
        # returns false if the position was occupied and it was not updated
        # override is a boolean that allows us to update even though position is occupied
        if (override == True) or (not isPositionOccupied(x,y)):
            self.matrx[x][y] = value
            return True
        else:
            return False

class Cell:
    cellType=0
    cellState='q' #cellState = {q:quinsient, p:proliferating, m:migrating}
    def __init__(self,cellType):
        self.cellType = cellType
    def __str__(self):
        print 'Cell Type: ',self.cellType,', Cell State: ',self.cellState
