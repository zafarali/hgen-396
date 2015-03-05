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

	def calculateH( self, cell1, cell2, otherOptions = {} ):
    #calculates the H between two spin cells.

		if Tools.kdelta( cell1.getSpin(), cell2.getSpin() ) != 1:
			interactionStrength = self.determineInteractionStrength( cell1, cell2 ) 
			
			extraEnergies = 0
			
			## execute custom functions.
			if self.specialFunctions:
				for _, extraEnergyFn in self.specialFunctions.items():
					extraEnergies = extraEnergies + extraEnergyFn( cell1, cell2, otherOptions )

			#return total energies
			return interactionStrength + extraEnergies
		else:
			return 0

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
