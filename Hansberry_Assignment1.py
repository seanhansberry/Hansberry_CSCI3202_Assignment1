# Sean Hansberry
# CSCI 3202

import sys
import Queue

def main(argv):
	#insure queue is working
	myQueue = Queue.Queue(0)
	for x in range(0,10):
		myQueue.put(x)
	print 'Queue size is: ', myQueue.qsize()
	for x in range(0,10):
		print 'Dequeuing item: ', myQueue.get()
	
	
	#insure stack class is working
	cStack=myStack()
	for x in range(0,10):
		cStack.push(x)

	print 'Number of items in stack: ', cStack.checkSize()
	
	for x in range(0,10):
		print 'Poping item from stack: ', cStack.attr1.pop()
	
	#insure Binary tree class is working
	rootNode = Node(0)
	myTree = binaryTree(rootNode)
	myTree.add(10,0)
	myTree.add(9,0)
	myTree.add(8,9)
	myTree.add(7,8)
	myTree.add(6,8)
	myTree.add(5,7)
	myTree.add(4,6)
	myTree.add(3,5)
	myTree.add(2,5)
	myTree.add(1,3)


	print 'Tree before delete'
	myTree.preOrder(rootNode)

	myTree.delete(1)
	myTree.delete(4)

	print 'Tree after delete'
	myTree.preOrder(rootNode)



	#insure graph is working
	myGraph = graph()
	for x in range(0,10):
		myGraph.addVertex(x)

	myGraph.addEdge(0, 1)
	myGraph.addEdge(0, 2)
	myGraph.addEdge(0, 3)
	myGraph.addEdge(1, 4)
	myGraph.addEdge(1, 5)
	myGraph.addEdge(1, 6)
	myGraph.addEdge(2, 7)
	myGraph.addEdge(2, 8)
	myGraph.addEdge(2, 9)
	myGraph.addEdge(2, 3)
	myGraph.addEdge(3, 4)
	myGraph.addEdge(3, 5)
	myGraph.addEdge(3, 6)
	myGraph.addEdge(3, 7)
	myGraph.addEdge(3, 8)
	myGraph.addEdge(3, 9)
	myGraph.addEdge(4, 5)
	myGraph.addEdge(4, 6)
	myGraph.addEdge(4, 7)
	myGraph.addEdge(4, 8)

	print 'After edges added graph is'
	print myGraph.key

	for x in range(0,5):
		myGraph.findVertex(x)

	return


class myStack():
	def __init__ (self):
		self.attr1 = []
	
	def push(self, valueToPush):
		self.attr1.append(valueToPush)
		
	def pop(self):
		self.attr1.pop()
	
	def checkSize(self):
		return len(self.attr1)
		
		
		
class Node():
	def __init__(self, integerKey, parent = None):
		self.integerKey = integerKey
		self.lChild = None
		self.rChild = None
		self.parent = parent
	
class binaryTree():
	
	def __init__(self, root_node):
		self.root = root_node
		self.nodeFound = False
	
	def add(self, value, parentValue):
		node = self.root
		self.nodeFound = False
		self.addRec(value, parentValue, node)
		if self.nodeFound == False:
			print 'Node not found'
	def addRec(self, value, parentValue, node):
		
		if node == None:
			return

		while node:
			if node.integerKey == parentValue:
				#found value try to add to tree
				self.nodeFound = True
				if node.lChild == None:
					node.lChild = Node(value, node)
					return
				elif node.rChild == None:
					node.rChild = Node(value, node)
					return
				else:
					print("Parent has two children, node not added")
					return
			#Node value not found yet
			else:
				self.addRec(value, parentValue, node.lChild)
				self.addRec(value, parentValue, node.rChild)
				return
					


	def delete(self, value, node = None):
		node = self.root
		self.nodeFound = False
		self.deleteRec(value, node)
		if self.nodeFound == False:
			print 'Node not found'
	
	def deleteRec(self, value, node):
		
		if node == None:
			return
		
		while node:
			if node.integerKey == value:
				self.nodeFound = True
				if node.lChild is not None:
					print("Node not deleted, has children")
					break
				elif node.rChild is not None:
					print("Node not deleted, has children")
					break
				else:
					if node.parent.lChild == node:
						node.parent.lChild = None
					elif node.parent.rChild == node:
						node.parent.rChild = None  
					print 'Node at value', value ,'deleted'
					break
			else:
				self.deleteRec(value, node.lChild)
				self.deleteRec(value, node.rChild)
				return
			
			

	def preOrder(self, node):
		if node != None:
			print node.integerKey
			self.preOrder(node.lChild)
			self.preOrder(node.rChild)

class graph():
	def __init__(self):
		self.key = {}
		self.adjacent = {}


	def addVertex(self, value):
		found = False

		for i, v in enumerate(self.key):
			if v == value:
				print("Vertex already exists")
				found = True
				break

		if found == False:
			#self.key[value]=None
			self.key[value] = []

			print'Added value:', value, '|| List is: ', self.key


	def addEdge(self, value1, value2):
		found1 = False
		found2 = False

		for i, v in enumerate(self.key):
			if v == value1:
				found1 = True
			elif v == value2:
				found2 = True

		if found1 and found2:
			self.key[value1].append(value2)
			self.key[value2].append(value1)
		else:
			print("One or more vertices not found")


	def findVertex(self, value):
		found = False
		for i, v in enumerate(self.key):
			if v == value:
				print 'Adjacent vertices for vertex',value, 'are', self.key[v]
				found = True
		if found == False:
			print 'Vertex', value, 'was not found.'



					
# main entry point
if __name__ == "__main__":
	main(sys.argv)
