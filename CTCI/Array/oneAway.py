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
			if diff>2:
				return False
		
	

str1 = "pale"
str2 = "plea"

print oneAway(str1, str2)