from Tools import Tools
import numpy as np

"""
    Cell represents cells on the lattice
"""

class Cell:
    DEFAULT_INFORMATION = {
        'mutationRate': 0.01 
    }
    
    START_STATE = 'q' #cellState = {q:quinsient, p:proliferating, m:migrating}
    

    def __init__( self, cellType , cellSpin  = 0 ):
        self.cellTimer = 0
        self.cellState = self.START_STATE
        self.cellType = cellType
        self.cellArea = 0
        self.cellSpin = cellSpin
    def __str__( self ):
        return '( Type: ' + str(self.cellType) + ',  State: ' + str(self.cellState) + ',  Area: ' + str(self.cellArea) + ', Spin: ' + str(self.cellSpin) + ' )'
    def __repr__( self ):
        return '( Type: ' + str(self.cellType) + ',  State: ' + str(self.cellState) + ',  Area: ' + str(self.cellArea) + ', Spin: ' + str(self.cellSpin) + ' )'
    def increaseArea( self, by = 1 ):
        self.cellArea += by
    def decreaseArea( self, by = 1):
        self.cellArea -= by
    def getType( self ):
        return self.cellType
    def getSpin( self ):
        return self.cellSpin
    def getArea( self ):
        return self.cellArea
    def isDead( self ):
        return self.cellArea == 0
    def getState(self):
        return self.cellState
        
    def evolve( self, **kwargs):
        if self.cellSpin == 0: 
            return
        
        mutationRate = kwargs.get('mutationRate')
        #this determines if the cell divides, grows or dies
        # does the cell become cancerous?
        
        if self.cellType != 2: # if not already mutated
           mutates = np.random.binomial( 1, mutationRate )
           if mutates:
               self.cellType = 2
               print self,'mutated'
        self.cellTimer += 1

    def interactWithGradient(self, gradient):
        pass
