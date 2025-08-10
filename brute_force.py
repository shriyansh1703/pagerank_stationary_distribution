import numpy as np
from ev_method import get_matrix


def get_initial(pages):
    r0 = []
    for i in range(pages):
        r0.append(1/pages)
    return np.array(r0)


def normalizer(matrix):
    return matrix/matrix.sum(axis=0)


if __name__ == "__main__":
    count = 0
    print("Enter the adjacency matrix of the Markov chain (give spaces between row elements): ")
    pages, A = get_matrix()
    trn_mat = normalizer(A)
    i = int(input("Enter the number of iterations: "))
    while count < i:
        pow_mat = np.linalg.matrix_power(trn_mat,count)
        col_vec = get_initial(pages).transpose()
        prod = np.linalg.matmul(pow_mat,col_vec)
        print(f"R{count} vector = {prod}")
        count += 1







