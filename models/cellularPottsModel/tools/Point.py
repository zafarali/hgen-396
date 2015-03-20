__author__ = 'zafarali'
__version__ = '0.0.1'

'''
Point
==========
This facilitates positions on a lattice.
Each position will have an x, y, z (optional) coordinate
We will have custom properties:
 1. spin - contains the spin of this point in the lattice (mutable)
 2. coordinate - tuple of x,y, z (optional) position
 3. x - x coordinate
 4. y - y coordinate
 5. z (optional) - z coordinate
 2. neighbours - all points which are neighbouring this (immutable)
'''

# templates for different neighbourhoods, values represent the distance to move from current point
__NEUMANN__ = [ ( 0, -1 ), ( 1, 0 ), ( -1, 0 ), ( 0 , 1 ) ]
__MOORE__ = [ ( 0, 1 ), ( 1, 0 ), ( 0, -1 ), ( -1, 0 ), ( 1, 1 ), ( -1, 1 ), ( -1, -1 ), ( 1, -1 ) ]

# returns a list of neighbours using a template
__MAPCORD__ = lambda x, y, templates: [ ( x + template[0], y + template[1] ) for template in templates ]

# returns if value is an edge case or not
__EDGE__ = lambda x, y, size: (x > size) or (x < 0) or (y > size) or (y < 0)

##### POINT ######
class Point:

	''' Initialization/Constructor
		@PARAMS
		x, y = x, y coordinate of this point
		spin = spin of this point
		size = size of the lattice this point will reside on (to check edge cases)
		method = for neighbour functions (only 2D atm): @TODO
			'moore' = returns moore neighbourhood (square)
			'neumann' = returns neumann neighbourhood (diamond)
	'''
	def __init__( self , x , y , spin, size, z = None, method = 'neumann' ):
		self.coordinate = ( x, y, z ) if z else ( x, y )
		self.x = x
		self.y = y
		self.z = z if z else None
		self.spin = spin
		neighbours = __MAPCORD__( x , y, __MOORE__ ) if method is 'moore' else __MAPCORD__( x, y, __NEUMANN__ )
		self.neighbours = [ neighbour for neighbour in neighbours if not __EDGE__( neighbour[0], neighbour[1], size )]

	def __repr__( self ):
		return str(self.coordinate) + ', spin=' +  str(self.spin)

	def __str__ ( self ):
		return self.coordinate + ', spin=' + str(self.spin)

	def setSpin( self, newSpin ):
		self.spin = newSpin
