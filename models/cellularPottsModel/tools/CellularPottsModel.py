from Lattice import Lattice
from Cell import Cell
from EnergyFunction import EnergyFunction
from Tools import Tools


class CellularPottsModel(Lattice):
    def __init__(self, size, energyFunction, specialObjects = {}):
        Lattice.__init__(self, size, energyFunction, specialObjects)

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
            'specialObjects': self.specialObjects,
            'cellList': self.cellList,
            'numberOfCells': self.numberOfCells,
            # the list comprehension below generates a list of celltarget areas
            # where the index corresponds to the spin and the value corresponds to the cell target
            'cellTargetAreaList': [ self.cellTargetAreaList[ (str(self.getCellWithSpin(i).getType())) ] for i in range(0, self.numberOfCells) ]
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
            H_final = H_final + self.energyFunction.calculateH( trialNeighbour, neighbourCell, options )

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
        print spinTrue
        selected_cell['Cell'].evolve()

    
    def runSimulation(self, MCS, method='moore', showVisualization=False):
        # 1 Monte Carlo Time Step = N Spin copy attempts
        for i in range(0, MCS * self.size):
            self.metropolis(method=method, showVisualization=showVisualization)
