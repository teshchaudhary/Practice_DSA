def transpose(mat):
    m = len(mat)

    temp = [[0 for i in range(m)] for i in range(m)]
    for i in range(m):
        for j in range(m):
            temp[i][j] = mat[j][i]
    
    for i in temp:
        print(i)
