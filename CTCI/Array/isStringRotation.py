def isSubstring(s1, s2):
	s = s1 + s2
	if s2 in s:
		return True
	else:
		return False

string1 = "waterbottle"
string2 = "erbottlewat"

print isSubstring(string1,string2)