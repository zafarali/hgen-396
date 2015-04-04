import numpy as np
class Tools:
    # @staticmethod
    # def rndm( l, r ):
    #     return int(round((r-l)*np.random.random() +l))
    # @staticmethod
    # def probability( threshold ):
    #     if (np.random.random() <= threshold) or threshold is 1:
    #         return True
    #     else:
    #         return False
    @staticmethod
    def boltzmannProbability( deltaH, temp ):
        if deltaH < 0:
            return 1
        else:
            return np.exp(float(-deltaH)/temp)
    # @staticmethod
    # def kdelta(a, b):
    #     '''This is an implementation of the Kronecker Delta Function 
    #     0 if a =/= b
    #     1 if a = b'''
    #     return 1 if a == b else 0
    @staticmethod
    def isEdgeCase(x, y, mn, mx):
        # checks if x or y are outside the bounds of mn and mx.
        return (x >= mx) or (x < mn) or (y >= mx) or (y < mn)
    # @staticmethod
    # def thetaFunction( x ):
    #     if x < 0:
    #         return 0
    #     else:
    #         return 1
    # @staticmethod
    # def poissonProbability(lamb):
    #     return np.random.poisson(lamb)
    # @staticmethod
    # def sqrt( arg ):
    #     return np.sqrt(arg).astype(int)
    @staticmethod
    def getNeighbourIndices(x, y, method='moore'):
        # returns the moore neighbourhood around x and y
        # WARN: this doesn't check for edge cases...
        if method is 'neumann':
            return [[x, y-1], [x, y+1], [x+1, y], [x-1, y]]
        else:
            return [[x, y+1], [x+1, y], [x,y-1], [x-1,y], [x+1,y+1], [x-1,y+1], [x-1, y-1], [x+1,y-1]]
