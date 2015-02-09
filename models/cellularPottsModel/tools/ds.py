__author__ = 'zafarali'
# Datastructure to help facillitate cellular potts


class Lattice:
    # constants
    DIMENSION = 2
    
    # attributes
    size = 0
    name = 'GenericLattice2D'
    
    
    def __init__(self, size):
        self.size = size
    
    def giveName(self, name):
        self.name = name
    
    def initialize(self, numberOfCells, cellBlockArea):
        #code to initialize lattice here
        self.matrix = [[0 for i in range(self.size)] for j in range(self.size)]
        pass
    

class Cell:
    cellType=0
    cellState='q' #cellState = {q:quinsient, p:proliferating, m:migrating}
    def __init__(self,cellType):
        self.cellType = cellType
    def __str__(self):
        print 'Cell Type: ',self.cellType,', Cell State: ',self.cellState