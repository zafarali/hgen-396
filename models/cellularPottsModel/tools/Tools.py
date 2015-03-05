import numpy as np
class Tools:
    @staticmethod
    def rndm( l, r ):
        return int(round((r-l)*np.random.random() +l))
    @staticmethod
    def probability( threshold ):
        if (np.random.random() <= threshold) or threshold is 1:
            return True
        else:
            return False
    @staticmethod
    def boltzmannProbability( deltaH, temp ):
        if deltaH < 0:
            return 1
        else:
            return np.exp(float(-deltaH/temp))
    @staticmethod
    def kdelta(a, b):
        '''This is an implementation of the Kronecker Delta Function 
        0 if a =/= b
        1 if a = b'''
        return 1 if a == b else 0
    @staticmethod
    def isEdgeCase(x, y, mn, mx):
        # checks if x or y are outside the bounds of mn and mx.
        return (x >= mx) or (x <= mn) or (y >= mx) or (y <= mn)
