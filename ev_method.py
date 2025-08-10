import numpy as np


def get_matrix():
    a = []
    rows = int(input("Enter the number of rows in the matrix: "))
    for i in range(rows):
        row = list(map(float,input(f"Enter row {i+1}: ").split()))
        a.append(row)
    return rows, np.array(a)


def google_matrix(pages,matrix):
    g = 0.85*(matrix) + (0.15/pages)*(np.ones((pages,pages)))
    return g


def ranker(pages, pi_norm):
    page_lst = [num for num in range(1,pages+1)]
    page_dist = list(zip(page_lst,pi_norm))
    page_dist.sort(key=lambda tup: tup[1], reverse=True)
    print("The pages are ranked in the following order: ")
    for i in range(len(page_dist)):
        if i != len(page_dist)-1:
            print(f"{page_dist[i][0]} > ", end=" ")
        else:
            print(f"{page_dist[-1][0]}")


def normalizer(matrix):
    return matrix/matrix.sum(axis=0)


if __name__ == "__main__":
    print("Enter the adjacency matrix of the Markov chain (give spaces between row elements): ")
    pages, A = get_matrix()
    trn_mat = normalizer(A)
    print("Transition matrix:")
    print(trn_mat)
    eigenvalues, eigenvectors = np.linalg.eig(trn_mat)
    pi = np.array([sub[0] for sub in eigenvectors])
    pi_norm = np.array([(num/np.sum(pi)).real for num in pi])
    print(f"Stationary probability distribution: {pi_norm}")
    ranker(pages,pi_norm)

