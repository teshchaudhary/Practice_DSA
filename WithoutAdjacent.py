# Find subsequence wth maximum sum that there should be no adjacent elements in the subsequence

def maximumSubarraySum(arr, n):
    inx = arr[0]
    ecx = 0
    
    for i in range(1, n):
        n_ecx = max(inx, ecx)
        
        inx = ecx + arr[i]
        ecx = n_ecx
    
    return max(inx, ecx)
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(maximumSubarraySum(arr,n))
