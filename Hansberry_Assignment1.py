# Sean Hansberry
# CSCI 3202

import sys
import Queue

def main(argv):
	#insure queue is working
	myQueue = Queue.Queue(0)
	myQueue.put(3)
	myQueue.put(4)
	print(myQueue.get())
	x = 0
	x=myQueue.qsize()
	print(x)
	
	
	#insure stack class is working
	cStack=myStack()
	cStack.push(10)
	cStack.push(20)
	cStack.push(30)
	
	cStack.checkSize()
	cStack.pop()
	cStack.checkSize()
	
	rootNode = Node(0)
	myTree = binaryTree(rootNode)
	myTree.add(15, 0)
	myTree.add(10,15)
	myTree.add(20, 20)
	
	myTree.delete(100)
	myTree.delete(0)
	myTree.delete(10)

	myTree.preOrder(rootNode)


	myGraph = graph()
	myGraph.addVertex(1)
	myGraph.addVertex(2)
	myGraph.addVertex(4)
	myGraph.addVertex(1)

	myGraph.addEdge(1,2)
	myGraph.addEdge(4,0)
	myGraph.addEdge(99,99)
	myGraph.addEdge(2,4)
	myGraph.addVertex(25)
	myGraph.findVertex(2)
	myGraph.findVertex(12)

	return


class myStack():
	attr1 = 0
	def __init__ (self):
		self.attr1 = []
	
	def push(self, valueToPush):
		self.attr1.append(valueToPush)
		
	def pop(self):
		self.attr1.pop()
	
	def checkSize(self):
		print(len(self.attr1))
		
		
		
class Node():
	def __init__(self, integerKey, parent = None):
		self.integerKey = integerKey
		self.lChild = None
		self.rChild = None
		self.parent = parent
	
class binaryTree():
	
	def __init__(self, root_node):
		self.root = root_node
		
	def add(self, value, parentValue, node = None):
		print(self.root.integerKey)
		print(parentValue)

		node = self.root


		while node:
			if node.integerKey == parentValue:
				#found value try to add to tree
				if node.lChild == None:
					node.lChild = Node(value, node)
					break
				elif node.rChild == None:
					node.rChild = Node(value, node)
					break
				else:
					print("Parent has two children, node not added")
					break
			#Node value not found yet
			else:
				if node.lChild is not None:
					node = node.lChild
				elif node.rChild is not None:
					node = node.rChild
				else:
					print("Parent not found")
					break

	def delete(self, value):
		node = self.root
		while node:
			if node.integerKey == value:
				if node.lChild is not None:
					print("Node not deleted, has children")
					break
				elif node.rChild is not None:
					print("Node not deleted, has children")
					break
				else:
					node = None
					print 'Node at value', value ,'deleted'
					break
			else:
				if node.lChild is not None:
					node = node.lChild
				elif node.rChild is not None:
					node = node.rChild
				else:
					print("Node not found")
					break

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

			print'added value:', value, 'List is: ', self.key


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
