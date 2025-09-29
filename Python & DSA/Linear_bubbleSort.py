arr = [99,23,45,78,12,11,13]
n = len(arr)

# Outer loop
for i in range(n-1): # beacuse last is alredy sorted
  # inner loop
  for j in range(n-1-i):# n-1-i for don't check again fixed element
    if arr[j] < arr[j+1]
    arr[j] ,arr[j+1] = arr[j+1],arr[j]
    print(j,j+1,arr)
print(arr)
  
  
