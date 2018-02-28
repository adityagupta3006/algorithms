# It picks an element as pivot and partitions 
# the given array around the picked pivot.

array = [10, 7, 8, 9, 1, 5]

def quickSort(arr, l, h):
	if l<h:
		pivot = arr[h]
		i = 0
		for j in range(h):
			if arr[j] <= pivot:
				arr[i], arr[j] = arr[j], arr[i]
				i += 1
		arr[i], arr[h] = arr[h], arr[i]
		quickSort(arr, l, i-1)
		quickSort(arr, i+1, h)
		return arr
arr = quickSort(array, 0, len(array)-1)
print arr