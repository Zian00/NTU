import time
import importlib
from lab.lab6.qn1 import dual_search_q1
from q2 import dual_search_q2, merge, mergeSort

# Function to read values from a file
def read_values(filename):
    with open(filename, 'r') as file:
        return list(map(int, file.readlines()))

# Function to evaluate performance
def evaluate_performance(algorithm_function, data):
    start_time = time.time()
    algorithm_function(data, len(data), 8, [])  # Call the function directly
    end_time = time.time()
    return end_time - start_time

# Load data from input files
input_1mil = read_values('input_1mil.txt')
input_500k = read_values('input_500k.txt')


# Evaluate performance for input_1mil
print("Evaluating performance for input_1mil.txt:")
q1_time_1mil = evaluate_performance(dual_search_q1, input_1mil)
q2_time_1mil = evaluate_performance(dual_search_q2, input_1mil)
print(f"q1.py running time: {q1_time_1mil:.4f} seconds")
print(f"q2.py running time: {q2_time_1mil:.4f} seconds")


# Evaluate performance for input_500k
print("\nEvaluating performance for input_500k.txt:")
q1_time_500k = evaluate_performance(dual_search_q1, input_500k)
q2_time_500k = evaluate_performance(dual_search_q2, input_500k)
print(f"q1.py running time: {q1_time_500k:.4f} seconds")
print(f"q2.py running time: {q2_time_500k:.4f} seconds")