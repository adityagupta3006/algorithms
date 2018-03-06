def kSmallest(array, arraySize, k):
	if arraySize >= k:
		smallArray = array[:k]
		m = calcMax(smallArray)
		m_index = smallArray.index(m)
		for i in range(k, arraySize):
			if array[i] < m:
				smallArray[m_index] = array[i]
				m = calcMax(smallArray)
		return calcMax(smallArray)
	return  Falsxe 

def calcMax(data):
	m = data[0]
	for a in data:
		if a > m:
			m = a
	return m

def parseInput(data):
	num_iterations = data[0]
	for i in range(num_iterations):
		arraySize = data[1 + i*3]
		array = data[2 + i*3]
		k =  data[3 + i*3] 
		print kSmallest(array, arraySize, k)

inp = [2, 6, [7, 10, 4, 3, 20, 15], 3, 5, [7, 10, 4, 20, 15], 4]
parseInput(inp)