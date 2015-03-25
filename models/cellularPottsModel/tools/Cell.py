from Tools import Tools
import numpy as np


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
        
    def evolve( self, information=DEFAULT_INFORMATION, gradients=[]):
        #this determines if the cell divides, grows or dies
        # does the cell become cancerous?
        #if self.cellType != 2 and self.cellSpin != 0:
        #    mutates = np.random.binomial(1, Tools.poissonProbability(information['mutationRate']))
        #    if mutates:
        #        self.cellType = 2
        #        print self,'mutated'

        #for gradient in gradients:
        #    self.interactWithGradient(gradient)

        self.cellTimer += 1

    def interactWithGradient(self, gradient):
        pass
