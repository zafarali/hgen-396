import numpy as np

class Gradient:
	# creates a 1D gradient


	def __init__( self, gradientFunc, latticeSize, interactionStrength = 0):
		
		self.interactions = [gradientFunc(i) for i in range(0, latticeSize)]
		# print self.interactions
		self.interactionStrength = interactionStrength

	def interactionAt ( self, pos ):
		try:
			return self.interactions[pos] * self.interactionStrength
		except IndexError:
			if pos < 0:
				return self.interactions[0]
			elif pos > len(self.interactions:
				return self.interactions[len(self.interactions)]
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

'''end'''