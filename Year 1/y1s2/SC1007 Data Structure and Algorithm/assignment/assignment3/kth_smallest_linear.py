"""
input:
3 5
1  5  9
10 11 13
12 13 15

output:
11
"""

def kth_smallest(matrix, k):
    #insert your codes here
    n = len(matrix)
    
    # Define bounds for binary search
    low = matrix[0][0]  # Smallest element in matrix
    high = matrix[n-1][n-1]  # Largest element in matrix
    
    while low < high:
        mid = low + (high - low) // 2
        count = 0
        
        # Count elements smaller than or equal to mid
        for i in range(n):
            # For each row, find position where elements exceed mid
            j = n - 1
            while j >= 0 and matrix[i][j] > mid:
                j -= 1
            count += (j + 1)  # Count elements <= mid in this row
        
        # Adjust search space
        if count < k:
            low = mid + 1
        else:
            high = mid
    
    return low


#read the input
n, k = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
#output
print(kth_smallest(matrix, k))