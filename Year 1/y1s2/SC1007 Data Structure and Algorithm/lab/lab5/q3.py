import itertools
import time
import matplotlib.pyplot as plt

def knapsack_bruteforce(capacity, artifacts):
    """
    Brute-force approach for the 0/1 knapsack problem.
    
    Parameters:
      capacity (int): Maximum weight capacity of the backpack.
      artifacts (list): List of tuples (weight, value) for each artifact.
    
    Returns:
      max_value (int): Maximum achievable value.
      best_subset (list): List of artifacts (weight, value) in the best solution.
      best_weight (int): Total weight used in the best solution.
    """
    n = len(artifacts)
    max_value = 0
    best_subset = [] 
    best_weight = 0

    # Iterate over all possible subset sizes (from 0 to n)
    for r in range(n + 1):
        for subset in itertools.combinations(artifacts, r):
            total_weight = sum(item[0] for item in subset)
            total_value = sum(item[1] for item in subset)
            if total_weight <= capacity and total_value > max_value:
                max_value = total_value
                best_subset = list(subset)
                best_weight = total_weight

    return max_value, best_subset, best_weight

def read_test_cases(filename):
    """
    Reads the file with multiple test cases.
    Each test case is separated by an empty line.
    
    The first line of a test case is the backpack capacity,
    and each subsequent line contains "weight value" of an artifact.
    
    Returns a list of tuples (capacity, artifacts).
    """
    with open(filename, "r") as file:
        content = file.read().strip()
    
    # Split the file into test cases by blank lines.
    raw_cases = content.split("\n\n")
    print(f"raw cases: {raw_cases}")
    test_cases = []
    for case in raw_cases:
        lines = case.strip().splitlines()
        print(f"lines here: {lines}")
        if not lines:
            continue
        capacity = int(lines[0].strip())
        artifacts = [tuple(map(int, line.strip().split())) for line in lines[1:]]
        test_cases.append((capacity, artifacts))
    return test_cases

# Read test cases from q3input.txt
filename = "q3input.txt"
test_cases = read_test_cases(filename)

# To store execution times and number of artifacts for plotting.
execution_times = []
artifact_counts = []

# Process each test case.
for index, (capacity, artifacts) in enumerate(test_cases, start=1):
    start_time = time.time()
    max_value, best_subset, best_weight = knapsack_bruteforce(capacity, artifacts)
    exec_time = time.time() - start_time

    print(f"--- Test Case {index} ---")
    print("Backpack Capacity:", capacity)
    print("Artifacts:", artifacts)
    print("Maximum Value:", max_value)
    print("Selected Items (weight, value):", best_subset)
    print("Total Weight Used:", best_weight)
    print("Execution Time: {:.5f} sec\n".format(exec_time))

    execution_times.append(exec_time)
    artifact_counts.append(len(artifacts))

# Plot the execution times vs. number of artifacts.
# plt.figure(figsize=(8, 5))
# plt.plot(artifact_counts, execution_times, marker='o', linestyle='-')
# plt.xlabel("Number of Artifacts")
# plt.ylabel("Execution Time (sec)")
# plt.title("Brute-Force Knapsack: Execution Time vs. Number of Artifacts")
# plt.grid(True)
# plt.show()
