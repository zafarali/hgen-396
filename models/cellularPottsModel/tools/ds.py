__author__ = 'zafarali'
# Datastructure to help facillitate cellular potts

import numpy as np

class Lattice:
    # constants
    DIMENSION = 2
    CELL_AREA_DEFAULT = 9


    # attributes
    size = 0
    name = 'GenericLattice2D'
    
    
    def __init__(self, size):
        self.size = size
        #create the matrix of zeros (essentially a blank lattice)
        self.matrix = [[0 for i in range(self.size)] for j in range(self.size)]
        self.matrix = np.array(self.matrix)
    
    def giveName(self, name):
        self.name = name
    
    def initialize(self, numberOfCells, cellArea=CELL_AREA_DEFAULT):
        self.cellArea = cellArea
        self.numberOfCells = numberOfCells
        #code to initialize lattice here

        for i in range(1,numberOfCells+1):

            pass
        pass
    def isPositionOccupied(self, x, y):
        return bool(self.matrix[x][y])

    def setLatticePosition(self, x, y, value):
        if not isPositionOccupied(x,y):
            self.matrx[x][y] = value
            return True
        else:
            return False

