def count_valid_triplets_bs(nums, K):
    nums.sort()
    n = len(nums)
    count = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            target = K - nums[i] - nums[j]

            # Binary search for max c such that nums[k] <= target
            low = j + 1
            high = n - 1
            valid_k = j  # Start with j so if no c found, gives 0

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    valid_k = mid
                    low = mid + 1
                else:
                    high = mid - 1

            count += max(0, valid_k - j)

    return count
