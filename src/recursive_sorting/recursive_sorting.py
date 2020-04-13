# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    i = 0
    j = 0
    l = 0
    k = min(len(arrA), len(arrB)) - 1
    while(l <= k):

        if(arrA[i] < arrB[j]):
            merged_arr[l] = arrB[j]

        if(arrA[i] > arrB[j]):
            merged_arr[l] = arrA[i]
        i += 1
        j += 1
        l += 1
    # deal with the extra

    if(len(arrA) > len(arrB)):
        for i in range(k, len(arrA)):
            merged_arr[l] = arrA[i]
    if(len(arrB) > len(arrA)):
        for i in range(k, len(arrB)):
            merged_arr[l] = arrB[i]
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if(len(arr) == 1):
        return arr
    else:

        array1 = merge_sort(arr[0:len(arr)//2])
        array2 = merge_sort(arr[len(arr)//2:])
        array3 = merge(array1, array2)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    # [start, mid], [mid+1, end]
    # arr[start], arr[mid + 1] = arr[mid + 1], arr[start]

    # 1, 2, 5,  3, 4, 7, 9
    # 1, 2, 3,  5, 4, 7, 9

    i = start
    j = mid + 1
    # run through both partitions at the same time
    # put the smaller of the 2 items at the space before the first partition
    while(i < mid + 1):
        if(arr[i] < arr[j]):
            arr[i], arr[j] = arr[j], arr[i]

        if(arr[i] > arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j += 1

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO
    if(len(arr) == 1):
        return arr
    else:

        arr = merge_sort_in_place(arr, 0,           len(arr)//2)
        arr = merge_sort_in_place(arr, len(arr)//2, len(arr))
        arr = merge_in_place(arr)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
