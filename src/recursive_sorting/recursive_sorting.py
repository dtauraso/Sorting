# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # print(arrA, arrB)
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    i = 0
    j = 0
    l = 0
    minimum_size = min(len(arrA), len(arrB))
    # print(minimum_size)
    k = minimum_size - 1 if minimum_size > 0 else 0
    while(l <= k):
        # print('i', i, 'j', j, 'l', l, 'minimum_size', minimum_size)

        # while 1 of the arrays hasn't been visited
            # compare each item from both arrays alternating depending on the bigger item
        while(i < len(arrA) and j < len(arrB)):
            if(arrA[i] <= arrB[j]):

                merged_arr[l] = arrA[i]
                l += 1
                i += 1

            elif(arrA[i] > arrB[j]):

                merged_arr[l] = arrB[j]
                l += 1
                j += 1

    # deal with the extra
    if(i < len(arrA)):
        for m in range(i, len(arrA)):
                merged_arr[l] = arrA[m]
                l += 1
    elif(j < len(arrB)):
        for n in range(j, len(arrB)):
                merged_arr[l] = arrB[n]
                l += 1
    # print("final array", merged_arr)
    # print()
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # print(arr)
    if(len(arr) == 0):
        return arr
    if(len(arr) == 1):
        return arr
    else:

        array1 = merge_sort(arr[0           :len(arr)//2])
        array2 = merge_sort(arr[len(arr)//2:])
        # print('about to merge', array1, array2)
        arr = merge(array1, array2)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    # [start, mid], [mid+1, end]
    # arr[start], arr[mid + 1] = arr[mid + 1], arr[start]

    # 1, 2, 5,  3, 4, 7, 9
    # 1, 2, 3,  5, 4, 7, 9
    print(start, mid, end)
    print(arr)
    i = start
    j = mid + 1
    print(arr[start: mid], arr[mid: end], arr[start:end])

    # run through both partitions at the same time
    # put the smaller of the 2 items at the space before the first partition
    while(i < mid + 1 and j < end):
        # print(i, j, len(arr))
        if(arr[i] <= arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1


        elif(arr[i] > arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    print(arr[start: mid], arr[mid: end], arr[start:end])
    print()
    # i: [start, mid]
    # j: [mid + 1, end]

    # if(i < mid + 1):
    #     for m in range(i, mid + 1):

    #             merged_arr[l] = arrA[m]
    #             l += 1
    # elif(j < len(arrB)):
    #     for n in range(j, len(arrB)):
    #             merged_arr[l] = arrB[n]
    #             l += 1
    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO
    # print(l, r)
    if(l > r):
        return arr

    elif(l == r):
        return arr
    else:
        mid = (l + r) // 2
        arr = merge_sort_in_place(arr, l, mid)
        arr = merge_sort_in_place(arr, mid + 1, r)
        arr = merge_in_place(arr, l, mid, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
