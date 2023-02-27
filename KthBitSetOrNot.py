# Using Left Shift Operator

def check1(n,k):
	if n & (1<<(k-1)):
		print("SET")
    
	else:
		print("NOT SET")


# Using Right Shift Operator

def check2(n,k):
	if n>>(k-1) & 1:
		print("SET")
	else:
		print("NOT SET")

check1(10,3)
check2(10,4)
