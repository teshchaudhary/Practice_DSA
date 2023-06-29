def isDivisible(s):
	   evenPos = oddPos = 0
	   
	   for i in range(len(s)):
	       if s[i] == '1':
	           if i & 1 == 1:
	               evenPos += 1
	           
	           else:
	               oddPos += 1
	   
	   return 1 if abs(evenPos - oddPos) % 3 == 0 else 0
	               
