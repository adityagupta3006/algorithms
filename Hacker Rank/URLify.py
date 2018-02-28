'''
Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith"
Output: "Mr%20John%20Smith" 
'''
def url(query):
	for a in query:
		if a == " ":
			query = query.replace(a, "%20")
	return query
#text = raw_input("enter the search query")
text = "Mr John Smith"
print url(text)