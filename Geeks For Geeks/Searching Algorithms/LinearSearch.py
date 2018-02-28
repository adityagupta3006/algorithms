#Given an array arr[] of n elements, write a function to search a given element x in arr[].
array = [1,2,3,4,5]
l = len(array)-1
s = 3
def LinearSearch(arr, search):
	for a in range(l-1):
		if arr[a] == search:
			return a
print LinearSearch(array, s)