def permutations(arr):
	if len(arr) == 0:
		return []

	if len(arr) == 1:
		return [arr]
	l = []	
	for i in range(len(arr)):
		m = arr[i]
		rem = arr[:i] + arr[i+1:]
		for p in permutations(rem):
			l.append([m]+p)

	return l
data = [1,2,3]

print permutations(data)