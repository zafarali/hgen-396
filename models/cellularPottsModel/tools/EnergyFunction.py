from Tools import Tools
from Cell import Cell

class EnergyFunction:
	#this is a class to manipulate the energy function

	#energies is a dictionary of (key, value) pairs where key = energy, 
	#value = pair of cell types

	# specialFunctions is a list of extra energy functions.

	def __init__( self, energies , specialFunctions = None):
		self.energies = {}
		for energy, typePair in energies.items():
			x, y = typePair
			index = ''.join([str( x ) , ',' , str( y )])
			self.energies[ index ] = float(energy)

		self.specialFunctions = specialFunctions

	def pairWiseEnergy( self, cell1, cell2 ):
		return self.determineInteractionStrength( cell1, cell2 ) if cell1.getSpin() == cell2.getSpin() else 0

	
	def calculateH( self, cell, neighbours, otherOptions = {} ):
  	#calculates the H between current cell and neighbours
		neighbourInteractionStrength = 0

		for neighbour in neighbours:
			neighbourInteractionStrength += self.pairWiseEnergy(cell, neighbour)

		print 'H_neighbours=',str(neighbourInteractionStrength)
		extraEnergies = 0
		
		## execute custom functions.
		if self.specialFunctions:
			for _, extraEnergyFn in self.specialFunctions.items():
				newEnergyTerm = extraEnergyFn( cell, otherOptions )
				extraEnergies = extraEnergies + newEnergyTerm
				print 'H_',str(extraEnergyFn),'=',str(newEnergyTerm)

		#return total energies
		return neighbourInteractionStrength + extraEnergies


	def determineInteractionStrength( self, cell1, cell2 ):

		# following try catch allows us to key 1,2 or 2,1 
		indexTest = ''.join([str( cell1.getType() ), ',' , str( cell2.getType() )])
		
		strength = self.energies.get( indexTest , 'tryagain' )

		if strength is 'tryagain':
			indexTest = ''.join([str( cell2.getType() ), ',' , str( cell1.getType() )])
			strength = self.energies.get( indexTest, 'tryagain' )

		if strength is 'tryagain':
			return 0
		else:
			return strength
