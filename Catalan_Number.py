def findCatalan(n):
      res = 1
    	cat_ = 1
    
    	for i in range(1, n+1):
    		cat_ *= (4 * i - 2)
    		cat_ //= (i + 1)
    
    		res = cat_
    	
    	return res%1000000007
