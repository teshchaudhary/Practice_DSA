def OneOddOccuring(arr):
	num = 0
	
	for element in arr:
		num = num ^ element

	return num

arr = [1,2,3,1,2]

print(OneOddOccuring(arr))
