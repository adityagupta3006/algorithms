def rotate(arr):
	n = len(arr)
	for i in range(n/2):
		for j in range(i, n-i-1):
			t = arr[i][j]
			arr[i][j] = arr[n-j-1][i]
			arr[n-j-1][i] = arr[n-i-1][n-j-1]
			arr[n-i-1][n-j-1] = arr[j][n-i-1] 
			arr[j][n-i-1] = t			
	return arr
data = [[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,16]]
#data = [[1,2,3], [4,5,6], [7,8,9]]
for i in data:
	print i
print '\n'
rotatedData = rotate(data)
for i in rotatedData:
	print i