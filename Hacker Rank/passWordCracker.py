s = "wedowhatwemustbecausewecan"
i = ["because", "can", "do", "must", "we", "what"] 

def strMat(s, n):
	arr = []
	location = s.find(i[n])
	
	if location and n < len(i)-1:
		length = len(i[n])
		arr.append(strMat(s[:location], n+1))
		arr.append(s[location:location+length])
		arr.append(strMat(s[location+length:], n+1))
		
	print(arr)
	print("\n")

#strMat(s, 0)