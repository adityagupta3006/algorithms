def revString(string):
	array = string.split('.')
	l = len(array)
	for i in range(l/2):
		array[i], array[l-i-1] = array[l-i-1], array[i]
	print '.'.join(array)


def parseInput(data):
	num_iterations = data[0]
	for i in range(num_iterations):
		revString(data[1 + i])
		print "\n"

inp = [2, "i.like.this.program.very.much", "pqr.mno"]
parseInput(inp)