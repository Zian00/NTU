def find_median_sorted_arrays(num1, num2):
    if len(num1) > len(num2):
        num1, num2 = num2, num1

    m, n = len(num1), len(num2)

    # total length = 7
    total_length = m+n
    # half = 4
    half = (total_length + 1) // 2

    # left = 0, right = 3
    left, right = 0, m

    while left <= right:
        # i = 1, j = 3
        i = (left + right) // 2
        #  j calculate the number of elements to take from num2
        j = half - i
        """
        When i is 0, it means no elements are taken from num1 for the left side, 
        so we use negative infinity to ensure it doesn't affect the maximum of the left side.
        
        When i equals m, all elements of num1 are in the left partition, so we set right_num1_min to infinity.
        Similarly for num2 with j.
        """
        left_num1_max = float('-inf') if i == 0 else num1[i-1]
        right_num1_min = float('inf') if i == m else num1[i]

        left_num2_max = float('-inf') if j == 0 else num2[j-1]
        right_num2_min = float('inf') if j == n else num2[j]

        if left_num1_max <= right_num2_min and left_num2_max <= right_num1_min:
            if total_length % 2 == 1:
                # odd partiton
                return float(max(left_num1_max, left_num2_max))
            else:
                # even partition
                return (max(left_num1_max, left_num2_max) + min(right_num1_min, right_num2_min)) / 2.0

        elif left_num1_max > right_num2_min:
            right = i-1

        else:
            left = i+1

    raise ValueError("Cannot find valid partition")

num1 = [1, 3, 8]
num2 = [7, 9, 10, 11]
output = find_median_sorted_arrays(num1, num2)
print(output)