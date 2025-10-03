class Node:
  def __init__(self,data):
    self.data = data
    self.next = Node
# create a nodes 
node1 = Node(10)
ndoe2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# connect the nodes to the liked list

node1.next = node2
next2.next = node3
next3.next = node4

# Print the linked list
current = node1 
while current is not None:
  print(current.data,end = "->")
  current = current.next
print("None")

