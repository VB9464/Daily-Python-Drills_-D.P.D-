arr = [45,65,23,12,22,11] 
n = len(arr)

for i in range(n-1): 
  min_index = i # assume 
  for j in range(i+1,n): # run loop from at 1 index not 0 to n 
    if arr[j] < arr[min_index]: # search and compaier 
      min_index = j # new mimum index
  arr[i] , arr[min_index] = arr[min_index] ,arr[i] # swap
print(arr)

