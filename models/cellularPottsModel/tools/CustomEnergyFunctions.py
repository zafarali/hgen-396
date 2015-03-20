from Tools import Tools
from Cell import Cell

class CustomEnergyFunctions:

	@staticmethod
	def AreaConstraint( cell1, options ):
		
		# variable unpacking (COMMENTED OUT TO SAVE MEMORY)
		# numberOfCells = int(options['numberOfCells'])
		# cellList = options['cellList']
		# cellAreaList = options['cellAreaList']

		# implementation based on Granier Glazier 1992
		total = 0

		for i in range(0, int(len(options['cellList']))):
			#get target area / max area of this cell type
			targetArea = options['cellTargetAreaList'][i]

			#calculate theta ahead to save computation time
			theta = Tools.thetaFunction( targetArea )

			
			if theta != 0 :
				# the to be squared term
				toBeSquared = options['cellList'][i].getArea() - targetArea
				print 'current=',str(options['cellList'][i].getArea()),'target=',str(targetArea),', toBeSquared=',str(toBeSquared)
				print 'theta=',theta
				total = total + ( toBeSquared * toBeSquared ) * theta

		return total

	@staticmethod
	def OxygenGradientInteract( cell1, options ):
		# total = 0
		return options['specialObjects']['OxygenGradient'].interactionAt(options['y'])

	@staticmethod
	def NutrientInteract( cell1, options ):
		return options['specialObjects']['NutrientGradient'].interactionAt(options['y'])


'''end'''