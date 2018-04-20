'''
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away. 
'''

def oneAway(a1, a2):
	d1 = createDict(a1)
	d2 = createDict(a2)
	diff = 0

	if len(d1) == len(d2):
		for a in d1:
			if a not in d2:
				diff += 1
		
	elif len(d1) < len(d2):
		for i in d2:
			if i not in d1:
				diff += 1
			
	elif len(d2) < len(d1):
		for i in d1:
			if i not in d2:
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

#print oneAway(str1, str2)
for c1, c2 in zip(str1, str2):
	print c1, c2