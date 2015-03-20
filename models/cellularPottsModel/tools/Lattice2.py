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

		self.matrix = [ [ Point( x, y, 0, size, method ) for y in range( 0, size ) ] for x in range( 0 , size ) ]
