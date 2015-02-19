__author__ = 'zafarali'
#To change this template use Tools | Templates.
#
#

import ds

x = ds.Lattice(14)
print 'x.size=',x.size
x.initialize(11, 2)
print 'x.matrix=',x.matrix
print 'x.cellList=',x.cellList
#print str(ds.Tools.rndm(5,10))
#print 'running probability with p=0.25'
#for i in range(1,10):
#    print str(ds.Tools.probability(0.25))
#print 'running probability with p=0.9'
#for i in range(1,10):
#    print str(ds.Tools.probability(0.9))


#testing for cells.
cell1 = ds.Cell(0)
cell2 = ds.Cell(0)
cell3 = ds.Cell(2)

print 'the following should print the same thing on two lines:'
print str(x.interactionStrength(cell1,cell3))
print str(x.interactionStrength(cell3,cell1))
print 'this should be different'
print str(x.interactionStrength(cell1,cell2))