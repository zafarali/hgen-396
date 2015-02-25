__author__ = 'zafarali'
#To change this template use Tools | Templates.
#
#

import ds

x = ds.Lattice(10)
print 'x.size=',x.size
#initialize with 1 cell
x.initialize(1)
print 'x.matrix=',x.matrix
print 'running simulation for 3 MCS'
x.runSimulation(3)
print 'x.matrix=',x.matrix
#print str(ds.Tools.rndm(5,10))
#print 'running probability with p=0.25'
#for i in range(1,10):
#    print str(ds.Tools.probability(0.25))
#print 'running probability with p=0.9'
#for i in range(1,10):
#    print str(ds.Tools.probability(0.9))


#testing for cells.
cell1 = ds.Cell(1)
cell2 = ds.Cell(1)
cell3 = ds.Cell(2)

print 'the following should print the same thing on two lines:'
print str(x.interactionStrength(cell1,cell3))
print str(x.interactionStrength(cell3,cell1))
print 'this should be different'
print str(x.interactionStrength(cell1,cell2))
