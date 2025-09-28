# linear Delit
# Deletion in an array

arr =[10,20,30,40,50,60,70]
n = len(arr)
pos = 2 # position of the deletion element

for i in range(pos, n-1): # pos =2, n-1 = 6
    print(i) # i = 2,3,4,5 
    arr[i] = arr[i+1] # arr[2] = arr[3], arr[3] = arr[4], arr[4] = arr[5], arr[5] = arr[6]
    
# after the loop [10,20,40,50,60,70,70]
arr = arr[:-1]
# after slicing [10,20,40,50,60,70]
print(arr)
