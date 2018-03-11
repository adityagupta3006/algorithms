def reverse(data):
	if data == '':
		return data
	else:
		return reverse(data[1:]) + data[0]

string =  "abcd"
print reverse(string)