s = "babad"
l = len(s)
d = {}
for i in s:
	if i not in d:
		d[i] = 1
	else:
		d[i] += 1
if 2 not in d.values() and l > 1:
	print "No palindrome"

result = ""
for i in s:
	print d[i], i