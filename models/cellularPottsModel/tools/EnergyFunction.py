from Tools import Tools
from Cell import Cell

class EnergyFunction:
	#this is a class to manipulate the energy function

	#energies is a dictionary of (key, value) pairs where key = energy, 
	#value = pair of cell types

	def __init__( self, energies ):
		self.energies = {}
		for energy, typePair in energies.items():
			x, y = typePair
			self.energies[ (str( x ) , ',' , str( y )) ] = float(energy)


	def calculateH( self, type1, type2 ):
    #calculates the H between two spin cells.
		if Tools.kdelta( spin1, spin2 ) != 1:
			return self.determineInteractionStrength( type1, type2 ) 
		else:
			return 0

	def determineInteractionStrength( self, type1, type2 ):

		# following try catch allows us to key 1,2 or 2,1 

		indexTest = ''.join([str( type1 ), ',' , str( type2 )])
		strength = self.energies.get( indexTest , 'tryagain' )
		print indexTest, str(strength)
		if strength is 'tryagain':
			strength = self.energies.get( ( str( type1 ) , ',' , str( type2 ) ), 'tryagain' )
		
		if strength is 'tryagain':
			return 0
		else:
			return strength
