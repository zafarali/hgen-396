__author__ = 'zafarali'
# Datastructure to help facillitate cellular potts

import numpy as np
import matplotlib.pyplot as plt

class Tools:
    @staticmethod
    def rndm( l, r ):
        return round((r-l)*np.random.random() +l)
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
        
        # code to initialize cell list
        self.cellList = [Cell(1) for i in range(1,numberOfCells+2)]
        
        
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
            print i
            
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
            
        
    def isPositionOccupied(self, x, y):
        return bool(self.matrix[x][y])
    def setLatticePosition(self, x, y, value, override=0):
        # Sets a lattice position (x,y) to value = value
        # returns true if position was not occupied and it was updated
        # returns false if the position was occupied and it was not updated
        # override is a boolean that allows us to update even though position is occupied
        print x,y,self.size
        if x < self.size and y < self.size:
            if (override == True) or (not self.isPositionOccupied(x,y)):
                self.matrix[x][y] = value
                self.cellList[value].increaseArea()
                return True
            else:
                return False
    def getNeighbourIndices(self, x, y):
        # returns the moore neighbourhood around x and y
        return [[x, y+1], [x+1, y], [x,y-1], [x-1,y], [x+1,y+1], [x-1,y+1], [x-1, y-1], [x+1,y-1]]
        
    def interactionStrength(self, cellA, cellB):
        #determines the interaction strenght between two cells
        pass
    def getCellAt(self, x, y):
        return self.cellList[self.matrix[x][y]]
#    def visualize(self):
#        heatmap, xedges, yedges = np.histogram2d(range(0,self.size), self.matrix[:][:], bins=50)
#        extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
#
#        plt.clf()
#        plt.imshow(heatmap, extent=extent)
#        plt.show()

class Cell:
    cellType=0
    cellState='q' #cellState = {q:quinsient, p:proliferating, m:migrating}
    
    def __init__(self,cellType):
        self.cellType = cellType
        self.cellArea = 0
    def __str__(self):
        return ' Type: ' + str(self.cellType) + ', State: ' + str(self.cellState)
    def __repr__(self):
        return '( Type: ' + str(self.cellType) + ',  State: ' + str(self.cellState) + ',  Area: ' + str(self.cellArea) + ' )'
    def increaseArea(self, by=1):
        self.cellArea += by
    def cellType(self):
        return cellType
