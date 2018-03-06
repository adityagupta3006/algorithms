def missingNumber(arr, n):
	s = (n*(n+1))/2
	for a in arr:
		s = s-a
	return s

def parseInput(data):
	num_iterations = data[0]
	for i in range(num_iterations):
		n = data[1 + 2*i]
		arr = data[2 + 2*i]
		print missingNumber(arr, n)

 
inp = [2, 5, [1,2,3,5], 10, [1,2,3,4,5,6,7,8,10]]
parseInput(inp)