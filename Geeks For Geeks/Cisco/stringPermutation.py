def stringPermutation(word):
    print "word = ", word
    if len(word) == 1:
        return [word]
    char = word[0]
    print "char = ", char 
    rest = stringPermutation(word[1:])
    print "rest = ", rest
    result = []

    for i in rest:
        for l in range(len(i)+1):
            result.append(i[:l]+char+i[l:])
            print "result = ", result
    
    return result

def parseInput(data):
	num_iterations = data[0]
	for i in range(num_iterations):
		l = len(data[1 + i])
		print stringPermutation(data[1 + i])
		print "\n"

inp = [2, "ABC", "ABSG"]
parseInput(inp)