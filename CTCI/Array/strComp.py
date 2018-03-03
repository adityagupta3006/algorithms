def strComp(string):
	count = 1
	prev = ''
	a = []
	for i in string:
		if prev == i:
			count += 1
			
		else:
			if count==1:
				if i != string[0]:
					a.append(count)
				a.append(i)
				
			if count>1:
				a.append(count)
				a.append(i)
				count = 1
		prev = i
	a.append(count)
	print a

strComp("aabcccccaaa")