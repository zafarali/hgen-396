__author__ = 'zafarali'
# Datastructure to help facillitate graph model


class Graph:
    nodes = []
    def __init__(self):
        pass
    def addNodes(self, nodeArray):
        self.nodes.extend(nodeArray)
    def printNodes(self):
        for node in self.nodes:
            node.printNode()

class Node:
    connections = []
    data = 'UninitializedData'
    def __init__(self, data):
        if data:
            self.data=data
        pass
    def printNode(self):
        print self.data,' connections: ', len(self.connections)
