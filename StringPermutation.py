'''
Given two strings, write a method to decide if one is a permutation of the other. 
'''

def permutation(a, b):
	dictionary_a = {}
	dictionary_b = {}
	for i in a:
		if i in dictionary_a:
			dictionary_a[i] += 1
		else:
			dictionary_a[i] = 1
	for i in b:
		if i in dictionary_b:
			dictionary_b[i] += 1
		else:
			dictionary_b[i] = 1

	return dictionary_a == dictionary_b
string_a = raw_input("Please enter the first string")
string_b = raw_input("Please enter the second string")
print permutation(string_a, string_b)