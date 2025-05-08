def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def dual_search_q2(A, size, K, dual_index):
    # A (list): The input array of integers.
    # size (int): The size of the array.
    # K (int): The target sum.
    # dual_index (list): A list to store the indices of the two elements
    new_A = mergeSort(A)
    for index, i in enumerate(new_A):
        for index2, j in enumerate(new_A):
            if ((i + j) == K):
                dual_index = [index, index2]
                return dual_index
    return "No pair found found"

A = [9, 1, 4, 3, 7, 5]
K = 8
dual_index = []


print(dual_search_q2(A, 6, K, dual_index))
