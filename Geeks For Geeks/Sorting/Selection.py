'''

Time Complexity: O(n^2)
Auxiliary Space: O(1)

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

'''

array = [10, 35, 30, 20, 15, 55]
l = len(array)

for a in range(l):
	minimum = a
	for b in range(a+1, l):
		if array[minimum] > array[b]:
			minimum = b
	array[a], array[minimum] = array[minimum], array[a] 
print array