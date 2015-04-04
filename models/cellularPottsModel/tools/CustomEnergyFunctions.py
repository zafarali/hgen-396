from Tools import Tools
from Cell import Cell
import numpy as np

class CustomEnergyFunctions:

	@staticmethod
	def AreaConstraint( cell1, options ):
		
		# implementation based on Granier Glazier 1992

		# stores the current area for each cell
		currentAreas = np.array([ cell.getArea() for cell in options['cellList'] ])
		print 'currentAreas=',currentAreas
		# stores the target area for each cell
		targetAreas = np.array(options['cellTargetAreaList'])
		print 'targetArea=',targetAreas

		# theta will remove the effects of negative areas
		theta = [ 0 if targetArea < 0 else 1 for targetArea in targetAreas ]
		# dot product of theta with (current-target)^2 to get the individual
		# parts of the hamiltonian 
		diffs = np.dot(theta, ((currentAreas - targetAreas)**2))
		# summation and conversion to integer form.
		return np.sum(diffs).astype(int)


	@staticmethod
	def OxygenGradientInteract( cell1, options ):
		# total = 0
		return options['specialObjects']['OxygenGradient'].interactionAt(options['x'])

	@staticmethod
	def NutrientInteract( cell1, options ):
		return options['specialObjects']['NutrientGradient'].interactionAt(options['x'])


'''end'''