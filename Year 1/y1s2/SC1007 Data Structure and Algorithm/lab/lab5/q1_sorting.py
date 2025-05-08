import time
import random
import pandas as pd
import matplotlib.pyplot as plt


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


result_bubble = []
result_merge = []

sample_size = [1000, 10000, 100000]
for size in sample_size:
    arr = [random.randint(1, 100) for _ in range(size)]
    start_bubble = time.perf_counter()
    bubble_sort(arr)
    end_bubble = time.perf_counter()
    execution_time = end_bubble - start_bubble
    result_bubble.append(execution_time)
    # print(f"Execution time: {execution_time} seconds")

for size in sample_size:
    arr = [random.randint(1, 100) for _ in range(size)]
    start_merge = time.perf_counter()
    merge_sort(arr)
    end_merge = time.perf_counter()
    execution_time = end_merge - start_merge
    result_merge.append(execution_time)
    # print(f"Execution time: {execution_time} seconds")


df = pd.DataFrame({
    'bubble_sort': result_bubble,
    'merge_sort': result_merge
}, index=sample_size)
lines = df.plot.line()
plt.show()
