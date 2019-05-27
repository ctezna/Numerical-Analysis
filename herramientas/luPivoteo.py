import pprint


def mult_matrix(M, N):
    tuple_N = list(zip(*N))
    return [[sum(el_m * el_n for el_m, el_n in zip(row_m, col_n)) for col_n in tuple_N] for row_m in M]

def pivot_matrix(M):
    m = len(M)
    id_mat = [[float(i ==j) for i in range(m)] for j in range(m)]
    for j in range(m):
        row = max(range(j, m), key=lambda i: abs(M[i][j]))
        if j != row:
            id_mat[j], id_mat[row] = id_mat[row], id_mat[j]

    return id_mat

def lu_decomposition(A):
    n = len(A)
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]
    P = pivot_matrix(A)
    PA = mult_matrix(P, A)
    for j in range(n):
        print("ETAPA:",j)
        L[j][j] = 1.0
        for i in range(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = PA[i][j] - s1
        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (PA[i][j] - s2) / U[j][j]
        print ("L:")
        pprint.pprint(L)
        print ("U:")
        pprint.pprint(U)
    return (P, L, U)

A = [[4,-1,0,3], [1,15.5,3,8], [0,-1.3,-4,1.1],[14,5,-2,30]]
P, L, U = lu_decomposition(A)