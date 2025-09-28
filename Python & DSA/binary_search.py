arr =[10,20,30,40,50,60]
x = 20
low = 0
high = len(arr) - 1
found = False

while low <= high:
  mid = (low + high)//2
  if arr[mid] == x :
    print(f"Element {x} found at {mid}")
    found = True
    break
  elif arr[mid] < x:
    low = mid + 1
  else:
    high = mid -1

if not found :
  print(f"element {x} is not found ") 
