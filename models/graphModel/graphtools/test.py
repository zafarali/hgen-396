__author__ = 'zafarali'
#To change this template use Tools | Templates.
#
#
import ds

g = ds.Graph()

print 'generating new nodes'
nodes = [ds.Node(x) for x in range(5)]
print nodes

print 'adding nodes to graphs'
g.addNodes(nodes)

g.printNodes()