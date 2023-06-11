def update(a, n, updates, k):
        prefix_sum = [0]*(n+1)
        
        for j in updates:
            prefix_sum[j-1] += 1
        
        for i in range(1,n):
            prefix_sum[i] += prefix_sum[i-1]
        
        for p in range(n):
            a[p] = prefix_sum[p]
