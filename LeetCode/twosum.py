def twoSum(data, target):
	data = data.sort()
	
	l = 0
	r = len(temp)-1
	while l<r:
		s = temp[l] + temp[r]
		if s == target:
			return temp[l], temp[r]
		if s < target:
			l = l+1
		else:
			r = r-1



nums = [3, 2 ,4]
temp = nums
print temp
target = 6
l, r = twoSum(nums, target)
print l, ' and ', r
print temp
#print nums.index(2)