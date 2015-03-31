from Tools import Tools
from Cell import Cell
import numpy as np

class CustomEnergyFunctions:

	@staticmethod
	def AreaConstraint( cell1, options ):
		
		# implementation based on Granier Glazier 1992

		currentAreas = np.array([ cell.getArea() for cell in options['cellList'] ])
		print 'currentAreas=',currentAreas
		targetAreas = np.array(options['cellTargetAreaList'])
		print 'targetArea=',targetAreas
		theta = [ 0 if targetArea < 0 else 1 for targetArea in targetAreas ]
		diffs = np.dot(theta, ((currentAreas - targetAreas)**2))
		return np.sum(diffs).astype(int)


	@staticmethod
	def OxygenGradientInteract( cell1, options ):
		# total = 0
		return options['specialObjects']['OxygenGradient'].interactionAt(options['y'])

	@staticmethod
	def NutrientInteract( cell1, options ):
		return options['specialObjects']['NutrientGradient'].interactionAt(options['y'])


'''end'''