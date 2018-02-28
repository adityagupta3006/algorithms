# The idea of Radix Sort is to do digit by digit sort starting 
# from least significant digit to most significant digit. 
# Radix sort uses counting sort as a subroutine to sort.
# O(d*(n+b))
array = [2, 10, 30, 15, 25, 30, 105, 102]
for i in array:
	print i%10