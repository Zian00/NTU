def dual_search_q1(A, size, K, dual_index):
    # A (list): The input array of integers.
    # size (int): The size of the array.
    # K (int): The target sum.
    # dual_index (list): A list to store the indices of the two elements
    for index, i in enumerate(A):
        for index2, j in enumerate(A):
            if ((i + j) == K):
                dual_index = [index, index2]
                return dual_index
    return "No pair found found"


A = [3, 1, 7, 4, 5, 9]
K = 8
dual_index = []
print(dual_search_q1(A, 6, K, dual_index))
