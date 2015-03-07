from Tools import Tools
from Cell import Cell

class CustomEnergyFunctions:

	@staticmethod
	def AreaConstraint( cell1, cell2, options ):
		
		# variable unpacking (COMMENTED OUT TO SAVE MEMORY)
		# numberOfCells = int(options['numberOfCells'])
		# cellList = options['cellList']
		# cellAreaList = options['cellAreaList']

		# implementation based on Granier Glazier 1992
		total = 0

		for i in range(0, int(options['numberOfCells'])):
			
			#get target area / max area of this cell type
			targetArea = options['cellTargetAreaList'][i]

			# the to be squared term
			toBeSquared = options['cellList'][i].getArea() - targetArea

			# the theta function
			theta = Tools.thetaFunction( targetArea )

			total = total + ( toBeSquared * toBeSquared ) * theta

		return total

'''end'''