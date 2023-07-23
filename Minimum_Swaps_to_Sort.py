def minSwaps(self, nums):
		numss = [[nums[i],i] for i in range(len(nums))]
		numss.sort()
		
		i = 0
		res = 0
		while i < len(nums):
		    j = numss[i][1]
		    
		    if j == i:
		        i += 1
		        continue
		    
		    numss[j], numss[i] = numss[i], numss[j]
		    res += 1
		 
		return res
