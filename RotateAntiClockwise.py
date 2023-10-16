# The last column becomes the first row
# The second last column becomes the second row

def rotate(mat):
    N = len(mat)
    temp = [[0]*N for i in range(N)]

    for i in range(N):
        for j in range(N):
            temp[N-j-1][i] = mat[i][j]
            
    for i in range(N):
        for j in range(N):
            print(temp[i][j], end = " ")
        print()
