def reverse(data):
	l = len(data)
	for i in range(l/2):
		data[i], data[l-i-1] = data[l-i-1], data[i]
	return data
A = [1, 2, 3, 4, 5, 6, 7]
print reverse(A)