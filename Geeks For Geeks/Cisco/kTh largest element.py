def kLargest(data, size, k):
	if size >= k:
		maxArray = data[:k]
		m = calcMin(maxArray)		
		for i in range(k, size):
			if data[i] > m:
				m_index = maxArray.index(m) 
				maxArray[m_index] = data[i]
				m = calcMin(maxArray)
		return m
	return '-1'

def calcMin(data):
	m = data[0]
	for i in data:
		if i < m:
			m = i
	return m


def parseInput(data):
	num_iterations = data[0]
	for i in range(num_iterations):
		k, arraySize = data[1 + i*2]
		array = data[2 + i*2]
		print kLargest(array, arraySize, k) , '\n'

inp = [2, [4,6], [1, 2, 3, 4, 5, 6], [1, 2], [3, 4]]
parseInput(inp)