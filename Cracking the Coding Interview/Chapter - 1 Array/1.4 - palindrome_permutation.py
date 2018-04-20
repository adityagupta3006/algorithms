def palindromePermutation(inp):
	dic = {}
	for i in inp:
		if i in dic:
			dic[i] += 1
		else:
			dic[i] = 1
	one = 0
	for i in dic:
		if dic[i]%2 == 1:
			one += 1
		if one>1:
			return False
	return True

string = " taco cat"
string = string.replace(" ", "")
print palindromePermutation(string)

#106,	 121, 134, 136