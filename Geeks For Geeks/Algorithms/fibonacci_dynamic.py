def fib(n):
	a = 0
	b = 1
	if n<0:
		return 
	elif n == 0:
		return a
	elif n == 1:
		return b
	else:
		for i in range(2,n):
			c = a+b
			a = b
			b = c
		return b
print fib(10)