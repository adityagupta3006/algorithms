def rearrange(data):
	l = len(data)
	m = -1
	for i in range(l):
		if arr[i] < 0:
			m += 1
			arr[i], arr[m] = arr[m], arr[i]

	pos = m+1
	neg = 0
	
	while (pos < l and neg < pos and arr[neg] < 0):
		arr[neg], arr[pos] = arr[pos], arr[neg]
		pos += 1
		neg += 2

	return arr

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
print rearrange(arr)