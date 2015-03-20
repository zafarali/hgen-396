__author__ = 'zafarali'
__version__ = '0.0.3'
'''
Lattice2
==========
This datastructure holds a 2D array of 'Point's
'''
from Point import Point

class Lattice2:

	DIMENSION = 2

	def __init__( self, size, template = None, method = 'neumann'):
		self.size = size
		self.matrix = [ [ Point( y, x, 0, size, method=method ) for y in range( 0, size ) ] for x in range( 0 , size ) ]

	def get( self, x, y ):
		return self.matrix[y][x]

	def setSpin ( self, x, y, newSpin ):
		self.get( x, y ).setSpin( newSpin )

