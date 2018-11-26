
class node:
	def __init__(self,data=None):
		self.data=data
		self.nextNode=None

class linked_list:
	def __init__(self):
		self.headNode=node()

	# Adds new node containing 'data' to the end of the linked list.
	def append(self,data):
		new_node=node(data)
		currentNode=self.headNode
		while currentNode.nextNode!=None:
			currentNode=currentNode.nextNode
		currentNode.nextNode=new_node

	# Returns the length (integer) of the linked list.
	def length(self):
		currentNode=self.headNode
		total=0
		while currentNode.nextNode!=None:
			total+=1
			currentNode=currentNode.nextNode
		return total

	# Prints out the linked list in traditional Python list format.
	def display(self):
		elems=[]
		current_node=self.headNode
		while current_node.nextNode!=None:
			current_node=current_node.nextNode
			elems.append(current_node.data)
		print (elems)

my=linked_list()
my.append(1)
my.append(2)
my.append(2)
my.append(4)
my.display()










