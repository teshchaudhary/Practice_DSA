# If there is any 1 in any row then convert each element of that row as 1

def func(mat):
    m = len(mat)
    n = len(mat[0])
    
    for i in range(m):
        if sum(mat[i]) > 0:
            for j in range(n):
                mat[i][j] = 1
    
    return mat
    
for _ in range(int(input())):
    m, n = map(int, input().split())
    mat = []
    for _ in range(m):
        row = list(map(int, input().split()))
        mat.append(row)
    
    func(mat)
    
    for i in range(m):
        for j in range(n):
            print(mat[i][j], end = " ")
        
        print()
