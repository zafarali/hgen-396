import numpy as np

class Gradient:
	# creates a 1D gradient

	# interaction type: -1 for attractive (less energy to go in that direction)
	# interaction type: +1 for repulsive (more energy to go in that direction)
	def __init__( self, gradientFunc, latticeSize, interactionType = -1, interactionStrength = 0):
		
		self.interactions = [gradientFunc(i) for i in range(0, latticeSize)]
		# print self.interactions
		self.interactionStrength = interactionStrength
		self.interactionType = interactionType

	def interactionAt ( self, pos ):
		try:
			return self.interactions[pos] * self.interactionStrength * self.interactionType
		except IndexError:
			return 0

	def __repr__(self):
		string = '[ %s ]' % str(self.interactions)
		string += '\n %d ' % self.interactionStrength
		string += 'attractive' if self.interactionType == -1 else 'repulsive'

		return string	
	def __str__(self):
		string = ' %s ' % str(self.interactions)
		string += '\n %d ' % self.interactionStrength
		string += 'attractive' if self.interactionType == -1 else 'repulsive'
		return string

'''end'''