__author__ = 'zafarali'
#To change this template use Tools | Templates.
#
#

import ds

x = ds.Lattice(4)
print 'x.size=',x.size
x.initialize(4, 2)
print 'x.matrix=',x.matrix
print 'x.matrix[1]',x.matrix[1]
print 'x.matrix[1][2]=',x.matrix[1][2]
print 'Reassigning x.matrix[1][2]=1'
x.matrix[1][2] = 1
print 'x.matrix[1][2]=',x.matrix