def pow(x,n):
	if n == 1:
		return x
	if n%2 == 0:
		return pow(x, n/2) * pow(x, n/2)
	else:
		return pow(x, (n-1)/2) * pow(x, (n-1)/2) * x  
print pow(2.100, 3)