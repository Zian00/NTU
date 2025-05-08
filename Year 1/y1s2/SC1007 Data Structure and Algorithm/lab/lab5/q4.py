import itertools
import time
import matplotlib.pyplot as plt


def tsp_bruteforce(distance_matrix):
    """
    Solves the TSP using a brute-force approach.

    Parameters:
      distance_matrix (list of list of int): A 2D list where element [i][j] is the distance 
                                               from node i to node j.

    Returns:
      best_distance (int): The length of the shortest possible route.
      best_route (list of int): The route (excluding the implicit return to the starting point) 
                                that yields the best distance.
    """
    n = len(distance_matrix)
    nodes = list(range(1, n))  # excluding the starting node (warehouse at 0)
    best_distance = float('inf')
    best_route = None

    # Try every permutation of the nodes (i.e., every possible order to visit the locations)
    for perm in itertools.permutations(nodes):
        # Calculate total distance for route: warehouse (0) -> perm -> warehouse (0)
        # from warehouse to first location
        current_distance = distance_matrix[0][perm[0]]
        for i in range(len(perm) - 1):
            current_distance += distance_matrix[perm[i]][perm[i+1]]
        current_distance += distance_matrix[perm[-1]][0]  # return to warehouse

        # Update best distance and route if current route is shorter
        if current_distance < best_distance:
            best_distance = current_distance
            # starting at 0; note: return to 0 is implicit
            best_route = [0] + list(perm)

    return best_distance, best_route


def read_test_cases(filename):
    """
    Reads multiple test cases from a file.

    Each test case is separated by an empty line. The first line of a test case is the number of locations,
    and the following lines are the rows of the distance matrix.

    Returns:
      A list of test cases, where each test case is represented as a distance matrix (list of lists of int).
    """
    with open(filename, "r") as file:
        content = file.read().strip()

    # Each test case is separated by a blank line.
    raw_cases = content.split("\n\n")
    test_cases = []

    for case in raw_cases:
        lines = case.strip().splitlines()
        if not lines:
            continue
        num_locations = int(lines[0].strip())
        matrix = []
        for line in lines[1:]:
            # Convert each row to a list of integers
            matrix.append(list(map(int, line.strip().split())))
        # Optional: Check that the matrix size matches num_locations
        if len(matrix) != num_locations or any(len(row) != num_locations for row in matrix):
            raise ValueError(
                "Distance matrix size does not match number of locations.")
        test_cases.append(matrix)
    return test_cases


# Read the test cases from q4input.txt
filename = "q4input.txt"
test_cases = read_test_cases(filename)

# Lists to store execution time and number of locations for plotting.
execution_times = []
num_locations_list = []

# Process each test case.
for index, matrix in enumerate(test_cases, start=1):
    num_locations = len(matrix)
    print(f"--- Test Case {index} ---")
    print("Number of Locations:", num_locations)

    start_time = time.time()
    best_distance, best_route = tsp_bruteforce(matrix)
    exec_time = time.time() - start_time

    print("Shortest Distance:", best_distance)
    print("Best Route:", best_route)
    print("Execution Time: {:.5f} sec\n".format(exec_time))

    execution_times.append(exec_time)
    num_locations_list.append(num_locations)

# Plot the execution times vs. number of locations.
plt.figure(figsize=(8, 5))
plt.plot(num_locations_list, execution_times, marker='o', linestyle='-')
plt.xlabel("Number of Locations")
plt.ylabel("Execution Time (sec)")
plt.title("Brute-Force TSP: Execution Time vs. Number of Locations")
plt.grid(True)
plt.show()
