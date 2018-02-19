array = [56, 23, 33, 44, 58]
l = len(array)
for i in range(1, l):
	key = array[i]
	j = i-1
	while j>=0 and key<array[j]:
		array[j+1] = array[j]
		j -= 1
	array[j+1] = key
print array