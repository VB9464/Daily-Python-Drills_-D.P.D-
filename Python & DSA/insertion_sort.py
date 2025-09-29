arr =[2,8,9,4,5,1]
n = len(arr)

for i in range(1,n): # 1 for start from second elemnt
  key = arr[i]
  j = i -1

  while j >=0 and arr[j] > key:  # it will keep shifting larg elemnt to the right in to new arr
    arr[j+1] = arr[j]
    j = j-1
   arr[j+1] = key 
print(arr)
