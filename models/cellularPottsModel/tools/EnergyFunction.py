from Tools import Tools
from Cell import Cell

class EnergyFunction:
	#this is a class to manipulate the energy function

	#energies is a dictionary of (key, value) pairs where key = energy, 
	#value = pair of cell types

	# specialFunctions is a list of extra energy functions.

	def __init__( self, energies , specialFunctions = None):
		self.energies = {}
		for typePair, energy in energies.items():
			if len(typePair) == 1:
				raise DeprecationWarning('No longer support for reverse energy definitions')
			x, y = typePair.split(',')
			# these two indexes allow us to store x,y = e and y,x = e
			index = ''.join( [ str( x ) , ',' , str( y ) ] )
			index2 = ''.join( [ str(y) , ',' , str(y) ] )
			self.energies[ index ] = float(energy)
			self.energies[ index2 ] = float(energy)

		self.specialFunctions = specialFunctions

	def pairWiseEnergy( self, cell1, cell2 ):
		# J( cell1.type, cell2.type ) ( 1 - kdelta ( cell1.spin, cell2.spin ) )
		indexTest = ''.join([str( cell1.getType() ), ',' , str( cell2.getType() )])
		strength = self.energies.get( indexTest , 'tryagain' )
		return 0 if strength is 'tryagain' else strength

	
	def calculateH( self, cell, neighbours, otherOptions = {} ):
  	#calculates the H between current cell and neighbours
		neighbourInteractionStrength = 0
		print 'Neighbour Cells: ',neighbours
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
