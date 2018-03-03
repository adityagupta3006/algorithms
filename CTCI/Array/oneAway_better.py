'''
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away. 
'''

def oneAway(a1, a2):
	d1 = createDict(a1)
	d2 = createDict(a2)
	ld1 = len(d1)
	ld2 = len(d2)
	return calcDiff(d1, d2) if ld1>=ld2 else calcDiff(d2, d1)

def calcDiff(m, n):
	diff = 0
	for a in m:
		if a not in n:
			diff += 1

	if diff>1:
		return False
	else:
		return True

def createDict(d):
	dictionary = {}
	for i in d:
		if i in dictionary:
			dictionary[i] += 1
		else:
			dictionary[i] = 1
	return dictionary

str1 = "palks"
str2 = "pal"

print oneAway(str1, str2)