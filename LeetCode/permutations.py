def permutations(arr):
	l = len(arr)
	if l == 0:
		return []

	if l == 1:
		return [arr]

	permute = []	
	for i in range(l):
		m = arr[i]
		rem = arr[:i] + arr[i+1:]
		for p in permutations(rem):
			permute.append([m]+p)

	return permute
data = [1,2,3]

print permutations(data)