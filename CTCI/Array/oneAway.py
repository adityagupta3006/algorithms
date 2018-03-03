'''
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away. 
'''

def oneAway(a1, a2):
	d1 = {}
	for i in a1:
		if i in d1:
			d1[i] += 1
		else:
			d1[i] = 0

	d2 = {}
	for i in a2:
		if i in d2:
			d2[i] += 1
		else:
			d2[i] = 0

	
	if len(d1) == len(d2):
		diff = 0
		for a in d1:
			if a not in d2:
				diff += 1
		
	
	if len(d1) < len(d2):
		diff = 0 
		for i in d2:
			if i not in d1:
				diff += 1
			if diff>2:
				return False
	
	if len(d2) < len(d1):
		diff = 0 
		for i in d1:
			if i not in d2:
				diff += 1
	if diff>1:
		return False
	else:
		return True


str1 = "pale"
str2 = "bake"

print oneAway(str1, str2)