def strComp(string):
	count = 1
	prev = ''
	a = []
	for i in string:
		if prev == i:
			count += 1
			
		if prev != i:
			if count==1:
				a.append(i)
				

			if count>1:
				a.append(count)
				a.append(i)
				count = 1
		prev = i
	print a

strComp("aabcccccaaa")