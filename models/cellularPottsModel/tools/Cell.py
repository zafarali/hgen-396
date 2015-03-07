class Cell:
    cellType=0
    cellState='q' #cellState = {q:quinsient, p:proliferating, m:migrating}
    cellSpin = 0
    def __init__( self, cellType , cellSpin  = 0 ):
        self.cellType = cellType
        self.cellArea = 0
        self.cellSpin = cellSpin
    def __str__( self ):
        return '( Type: ' + str(self.cellType) + ',  State: ' + str(self.cellState) + ',  Area: ' + str(self.cellArea) + ', Spin: ' + str(self.cellSpin) + ' )'
    def __repr__( self ):
        return '( Type: ' + str(self.cellType) + ',  State: ' + str(self.cellState) + ',  Area: ' + str(self.cellArea) + ', Spin: ' + str(self.cellSpin) + ' )'
    def increaseArea( self, by=1 ):
        self.cellArea += by
    def getType( self ):
        return self.cellType
    def getSpin( self ):
        return self.cellSpin
    def getArea( self ):
        return self.cellArea
    def evolve( self, information={} ):
        #this determines if the cell divides, grows or dies
        # does the cell become cancerous?

        pass

