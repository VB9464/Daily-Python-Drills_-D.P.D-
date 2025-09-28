# Linear array
# Insertion in an array
# Time complexity: O(n)
# 
arr = [10,20,30,40]
n = len(arr)
x = 50
print(n)
pos = 1 # position of the insertion element
arr.append(0) # increase the size of the array by 1
for i in range(n, pos, -1):
    arr[i] = arr[i-1]
    print(i)
arr[pos] = x
print(arr)
