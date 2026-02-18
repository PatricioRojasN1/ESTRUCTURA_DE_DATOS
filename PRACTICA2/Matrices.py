A = [[5, 6, 1], 
    [3, 10, 1], 
    [2, 11, 3]]

B = [[1, 2, 17],
    [6, 5, 15],
    [3, 11, 12]]

C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

for i in range(len(A)):            
    for j in range(len(B[0])):       
        for k in range(len(B)):      
            C[i][j] += A[i][k] * B[k][j]

for lista in C:
    print(lista)