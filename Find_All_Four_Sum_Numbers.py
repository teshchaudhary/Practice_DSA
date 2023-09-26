def fourSum(self, arr, k):
    n=len(arr)
    arr.sort()
    ans=[]
    for i in range(n-3):
        if i>0 and arr[i]==arr[i-1]:
            continue
        for j in range(i+1,n-2):
            if j>i+1 and arr[j]==arr[j-1]:
                continue
            left=j+1
            right=n-1
            while left<right:
                curr_sum=arr[left]+arr[right]+arr[i]+arr[j]
                if curr_sum>k:
                    right-=1
                elif curr_sum<k:
                    left+=1
                else:
                    ans.append([arr[i],arr[j],arr[left],arr[right]])
                    while left<right and arr[left]==arr[left+1]:
                        left+=1
                    while left<right and arr[right]==arr[right-1]:
                        right-=1
                    left+=1
                    right-=1
    return ans
