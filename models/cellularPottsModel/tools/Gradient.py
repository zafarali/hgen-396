import numpy as np

class Gradient:
	# creates a 1D gradient


	def __init__( self, gradientFunc, latticeSize, interactionStrength = 1):
		self.interactions = [gradientFunc(i) for i in range(0, latticeSize)]
		# print self.interactions
		self.interactionStrength = interactionStrength

	def interactionAt ( self, pos ):
		try:
			return self.interactions[pos] * self.interactionStrength
		except IndexError:
			if pos < 0:
				return self.interactions[0] * self.interactionStrength
			elif pos >= len(self.interactions):
				return self.interactions[len(self.interactions)-1] * self.interactionStrength
			else:
				return 0

	def __repr__(self):
		string = '[ %s ]' % str(self.interactions)
		string += '\n %d ' % self.interactionStrength

		return string	
	def __str__(self):
		string = ' %s ' % str(self.interactions)
		string += '\n %d ' % self.interactionStrength
		return string


class Gradient2D(Gradient):
	# creates a 2D gradient

	def __init__( self, gradientFunc, latticeSize, interactionStrength = 1 ):
		# generate a surface for the potential
		z = [ [ gradientFunc( x, y ) for x in range( 0, latticeSize ) ] for y in range( 0 , latticeSize ) ]
		self.interactions = np.array(z)

		self.interactionStrength = interactionStrength

	def interactionAt ( self, x, y ):
		M = len(self.interactions)
		try:
			return self.interactions[x][y] * self.interactionStrength
		except IndexError:
			# we are possibly in an edge case
			if x < 0 and y < 0:
				return self.interactions[0][0] * self.interactionStrength
			elif x >= M and y >= M:
				return self.interactions[M-1][M-1] * self.interactionStrength
			elif x >= M and y < 0:
				return self.interactions[0][M-1] * self.interactionStrength
			elif y >= M and x < 0:
				return self.interactions[M-1][0] * self.interactionStrength
			else:
				return 0

'''end'''