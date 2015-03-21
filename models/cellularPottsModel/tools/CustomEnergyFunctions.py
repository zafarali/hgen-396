from Tools import Tools
from Cell import Cell
import numpy as np

class CustomEnergyFunctions:

	@staticmethod
	def AreaConstraint( cell1, options ):
		
		# variable unpacking (COMMENTED OUT TO SAVE MEMORY)
		# numberOfCells = int(options['numberOfCells'])
		# cellList = options['cellList']
		# cellAreaList = options['cellAreaList']

		# implementation based on Granier Glazier 1992
		total = 0
		currentAreas = np.array([ cell.getArea() for cell in options['cellList'] ])
		targetAreas = np.array(options['cellTargetAreaList'])
		theta = [ 0 if targetArea < 0 else 1 for targetArea in targetAreas ]
		diffs = np.dot(theta, ((currentAreas - targetAreas)**2))
		return np.sum(diffs).astype(int)

		# for i in range(0, int(len(options['cellList']))):
		# 	#get target area / max area of this cell type
		# 	targetArea = options['cellTargetAreaList'][i]

		# 	#calculate theta ahead to save computation time
		# 	theta = 0 if targetArea < 0 else 1
			
		# 	if theta != 0 :
		# 		# the to be squared term
		# 		toBeSquared = options['cellList'][i].getArea() - targetArea
		# 		# print 'current=',str(options['cellList'][i].getArea()),'target=',str(targetArea),', toBeSquared=',str(toBeSquared)
		# 		total = total + ( toBeSquared * toBeSquared ) * theta

		# print type(total)
		# return total

	@staticmethod
	def OxygenGradientInteract( cell1, options ):
		# total = 0
		return options['specialObjects']['OxygenGradient'].interactionAt(options['y'])

	@staticmethod
	def NutrientInteract( cell1, options ):
		return options['specialObjects']['NutrientGradient'].interactionAt(options['y'])


'''end'''