# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i, item in enumerate(arr):
    if(item == target):
      return i
  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  while(low <= high):

    mid = (low + high) // 2

    if(target < arr[mid]):
      high = mid - 1
    elif(target > arr[mid]):
      low = mid + 1
    elif(target == arr[mid]):
      return mid
  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  if(len(arr) == 1):
    return arr[0]
  # TO-DO: add missing if/else statements, recursive calls
  if(target < arr[middle]):
    return binary_search_recursive(arr, target, low, middle - 1)
  elif(target > arr[middle]):
    return binary_search_recursive(arr, target, middle + 1, high)
  elif(target == arr[middle]):
    return middle