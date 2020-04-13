
# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    # O(n*n) = O(n^2) time
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # i: [0, curr_index] 
        # O(n) time
        for j in range(smallest_index + 1, len(arr)):
            if(arr[smallest_index] > arr[j]):
                smallest_index = j


        # TO-DO: swap
        # a, b = b, a
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    # print(arr)



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    number_of_swaps = 1
    while(number_of_swaps > 0):
        number_of_swaps = 0
        for i in range(0, len(arr)-1):
            if(arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                number_of_swaps += 1
        # print(arr)

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr