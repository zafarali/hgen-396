'''
tools - contains a set of functions to support the models
@author Zafarali Ahmed
HGEN396 - Winter 2015
'''

def kdelta(a, b):
	'''This is an implementation of the 
		 Kronecker Delta Function 
		 0 if a =/= b
		 1 if a = b'''
	return 1 if a == b else 0

