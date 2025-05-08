"""
input:
6 2
1 2 2 2 3 4

output:
1
"""
def first_occurrence(arr, target):
    # insert your codes
    low, high = 0, len(arr) - 1
    result = -1  # Default if target not found

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid          # Found a match
            high = mid - 1        # But keep looking to the left
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


n, target = map(int, input().split())
arr = list(map(int, input().split()))
result = first_occurrence(arr, target)
print(result)
