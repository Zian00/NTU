"""
input :
5 9
1 2 3 4 5

output :
-1
"""


def find_smallest_greater(arr, x):
    # issue with the code is if x is not inside the list but in the range, it will return -1. which is wrong
    # insert your codes here
    low, high = 0, len(arr) - 1
    result = -1  # Default if target not found
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x and x == arr[len(arr)-1]:
            return -1
        elif arr[mid] == x:
            return arr[mid+1]
        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1
    return result


def find_smallest_greater_chatgpt(arr, x):
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            result = arr[mid]
            high = mid - 1
        else:
            low = mid + 1

    return result


# read input
n, x = map(int, input().split())
arr = list(map(int, input().split()))

# Output
print(find_smallest_greater(arr, x))
