__author__ = 'zafarali'
__version__ = '0.0.2'

from Lattice2 import Lattice2
from Cell import Cell
'''
CPM
======
This is the engine of the CPM, it contains all the data structures
and algorithms needed to manipulate it.
'''

CELL_TARGET_AREA = 10

class Engine:

	def __init__( self, **kwargs ):
		self.size = kwargs.get( 'size', 2 )
		method = kwargs.get( 'method', 'neumann' )
		# template = kwags.get( 'template', None )

		cellTargetArea = kwargs.get( 'cellTargetArea', CELL_TARGET_AREA )

		self.lattice = Lattice2( self.size, method = method )
		
		# if template:
		# 	self.lattice.useTemplate( template )
				
		# by default all cells are of type 1
		self.cellList = [ Cell( 0 if i==0 else 1, i, targetArea = cellTargetArea ) for i in range( 0, self.size ) ]


