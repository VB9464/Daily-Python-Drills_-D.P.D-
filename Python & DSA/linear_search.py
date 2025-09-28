arr = [10,20,30,40,50,60]
n = len(arr)
x = 20
found = False

for i in range(n):
  if arr[i] == x:
    print(f"element {x} is found at the index {i}")
    found = True
    break
if not found:
  print("element is not found")
