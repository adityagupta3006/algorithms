def getRange(arr, target, lower):
	l = len(arr)
	m = (l+1)/2 - 1
	arr[m]
	if arr[m] == target:
		print lower + m
	if arr[m] < target:
		getRange(arr[m+1: ], target, lower + m + 1)
	
    
arr = [5,7,7,8,8,10]
tar = 8
getRange(arr, tar, 0)