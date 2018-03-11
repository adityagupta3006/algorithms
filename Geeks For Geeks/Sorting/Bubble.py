# Bubble sort Time Complexity: O(n^2)
# Swap adjacent elements till sorting

array = [2,3,1,4,6,5]
l = len(array)

for i in range(l):
		for j in range(0, l-i-1):
			print "i = ", i
			print "j = ", j, 
			print 'array = ', array, '\n'
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
print array
