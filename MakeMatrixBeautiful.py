# A beautiful matrix is a matrix in which the sum of elements in each row and column is equal. Given a square matrix of size NxN. Find the minimum number of operation(s) that are required to make the matrix beautiful. In one operation you can increment the value of any one cell by 1.

def findMinOpeartion(matrix, n):
        total = 0
        row_sums = [0] * n
        col_sums = [0] * n
        
        for i in range(n):
            for j in range(n):
                total += matrix[i][j]
                row_sums[i] += matrix[i][j]
                col_sums[j] += matrix[i][j]
        
        row_maxSum = max(row_sums)
        col_maxSum = max(col_sums)
        
        return max(row_maxSum, col_maxSum) * n - total
