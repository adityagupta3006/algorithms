arr = [1,2,3,4,5]
def rotate(array):
	temp = array[0]
	for a in range(len(array)-1):
		array[a] = array[a+1]
	array[len(array)-1] = temp
	return array
print rotate(arr)