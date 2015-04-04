__author__ = 'zafarali'
__version__ = '0.0.2'
# Datastructure to help facillitate cellular potts

import numpy as np
import matplotlib.pyplot as plt
from Cell import Cell
from Tools import Tools

class Lattice:
    # constants
    DIMENSION = 2
    CELL_AREA_DEFAULT = 20
    DEFAULT_TEMPERATURE = 10

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
        return Tools.isEdgeCase(x,y,0,self.size)

    def deepCopy(self, name='GenericLattice2D'):
        copy = Lattice(self.size, self.energyFunction)
        copy.initialize(self.numberOfCells, name=name)
        copy.matrix = np.copy(self.matrix)
        return copy

    def allCellsDead(self):
        cellsDead = [cell.isDead() for cell in self.cellList]
        # print cellsDead
        # returns true if all values in cellAlive are 1.
        return sum(cellsDead) >= self.numberOfCells 

    def initialize(self, numberOfCells, **kwargs):
        self.cellTargetAreaList = kwargs.get('cellTargetAreaList', {'0': -1, '1': self.CELL_AREA_DEFAULT, '2': self.CELL_AREA_DEFAULT})
        method = kwargs.get('method', 'random')
        self.name = kwargs.get('name', 'GenericLattice2D')
        self.numberOfCells = numberOfCells
        
        # code to initialize cell list
        self.cellList = [Cell(1, i) for i in range(0,numberOfCells+1)]
        print self.cellList
        self.cellList[0] = Cell(0)
        
        #code to initialize lattice here
        cycle = 1
        # we start from the middle of the lattice
        cellIndex = [self.size/2, self.size/2]

        # this 'method' distributes cells randomly around the center of the lattice
        if method is 'random':
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
        
        # this method sets the area between left, right, top and bottom with
        # value of spin.
        def populate ( left, right, top, bottom, spin ):
            for y in range( top, bottom ):
                for x in range( left, right ):
                    self.setLatticePosition( x, y, spin )           

        if method is 'custom':
            N, M = numberOfCells, self.size

            # get the starter areas for each cell spin
            # we first check if we are supplied with a list of starter areas
            # or else we just default to the same starter area for each cell
            a = kwargs.get( 'starterAreas', [ kwargs.get( 'starterArea', 4 ) for i in range( N + 1 ) ] )
            sqrta = np.sqrt(a).astype(int).tolist()
            a[0], sqrta[0] = -1, -1
            positions = kwargs.get( 'pos', 'failed' )
            if positions is 'failed':
                raise KeyError('When using method=custom, you must supply positions for each cell')
            elif len(positions) != N:
                raise ValueError('number of positions supplied must be the same as the number of cells')
            else:
                for i in range( 1, N + 1 ):
                    x, y = positions[ i - 1 ]
                    if self.isEdgeCase( x , y ):
                        raise ValueError(str(x) + ',' + str(y) + ' are not in the range of the lattice')
                    populate( x, x + sqrta[i], y, y + sqrta[i], i )
                    print x, y, i                    

        # this 'method' packs all the cells in the center of the lattice
        if method is 'central':
            N = numberOfCells
            sqrtN = np.sqrt( numberOfCells ).astype(int)

            M = self.size

            # starter areas of each cell spin, leaving out zero
            a = kwargs.get('starterAreas', [ kwargs.get( 'starterArea', 6 ) for i in range(N + 1) ] )
            sqrta = np.sqrt(a).astype(int).tolist()
            
            # setting the 0th position to refer to the ECM
            a[0], sqrta[0] = -1, -1

            startValue = int(0.25 * (M - sqrtN))
            startingPositions = kwargs.get( 'pos' , ( startValue , startValue ) )

            # checking boundaries, we can't place cells off the grid
            if self.isEdgeCase( startingPositions[0] , startingPositions[1] ):
                print 'Specified out of range pos, defaulting to precomputed values'
                startingPositions = ( startValue , startValue )

            x0, y0 = startingPositions

            # print x0,y0


            # print 'a side has length:'+str(sqrtN*np.average(sqrta).astype(int))
            # here we start populating the grids with spins.
            print sqrtN        
            for i in range(1,N+1):
                populate( x0, x0 + sqrta[i], y0, y0 + sqrta[i], i )
                x0 = x0 + sqrta[i]
                if x0 > (sqrtN * np.average(sqrta).astype(int)):
                    y0 = y0 + np.average(sqrta).astype(int)
                    x0 = startValue
                print x0, y0, i

        # for visualizing the matrix 
        plt.figure(self.name)
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
    def getCellTypeForSpin(self,spin):
        cell = self.getCellWithSpin(int(spin))
        return cell.getType()

    def visualize(self, hold=False):
        self.imageRep.set_data(self.matrix)
        plt.figure(self.name)
        if not hold:
            plt.draw()
            plt.pause(0.01)
        else:
            plt.draw()
            plt.show()

    def saveData (self, filename=None, what='lattice'):
        import time
        import csv
        filename = str(filename)+'_'+str(time.time()) if filename else str(time.time())
        if ( what is 'lattice' ) or ( what is 'all' ):
            # save lattice data to a file
            c = csv.writer ( open( filename+'_lattice.csv', "wb" ) )
            c.writerow( [ self.numberOfCells] )
            for row in self.matrix:
                c.writerow( row.tolist() )
            print 'Written Information'

        if ( what is 'cells' ) or ( what is 'all' ):
            #save cell data to a file
            c = csv.writer(open(filename+'_cells.csv', "wb"))
            c.writerow( ['spin', 'type', 'state', 'area', 'isDead'] )
            for cell in self.cellList:
                c.writerow([cell.getSpin(), cell.getType(), cell.getState(), cell.getArea(), cell.isDead()])
            


