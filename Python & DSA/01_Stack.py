# A stack follows LIFO ( Last in First Out ) principle
# Push ---> add item
# Pop  ---> remove item
# Peek ---> see top item

# Stack implementation using Python list
stack = [10,20,30] #empty stack

# Push elements
stack.append(50) # push 10
stack.append(60)
stack.append(70)
print("Stack after pushes:",stack)

#Pop element
print("Popped element:", stack.pop()) # removes 30
print("Stack after pop:", stack)

# Peek element (top of stack)
print("Top element:",stack[-1]) #last element
