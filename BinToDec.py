def conv(n):
	num = 0
	power = 0
	while (n != 0):
		if (n % 10 == 1):
			num += (1 << power) # Exponent of two
		power = power + 1
		n //= 10
		
	return num

num = 1010
print(conv(num))
