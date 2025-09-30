def merge_sort(arr):
    # First case : if input array is empty or in that one element
    if len(arr) <= 1:
        return arr
    
    # second step: divide array in two halves or parts
    mid = len(arr) // 2 # divide array an fix mid index
    left_half = arr[:mid] # from zero to mid
    right_half = arr[mid:] # from mid to end
    
    # Recursively sort both halves
    left_sorted = merge_sort(left_half) # 
    right_sorted = merge_sort(right_half) #

    return merge(left_sorted, right_sorted)

def merge(left_half, right_half):
    new = [] # for storeing merged array
    i=j= 0 # 
    while i < len(left_half) and j< len(right_half): # till run loop at last element of both half
        if left_half[i] < right_half[j]: # compare each element in of the both half array
            new.append(left_half[i])    # if left array element found smaller then add it in to new array
            i += 1 #i = i+1   # move torwards on next element in left_half
        else:
            new.append(right_half[j])  # if right array element found smaller then add it in to new array
            j+= 1 # j = j+1  # move torwards on next element in right_half

    new.extend(left_half[i:]) # it for if any element is left in left_half 
    new.extend(right_half[j:]) # if for if any elemnent is left in right_half.
    return new

arr = [38,27,43,3,9,82,10]
sorted_arr = merge_sort(arr)
print(sorted_arr)
print(merge_sort(arr))
