data = [[1,0,3,4], [5,6,0,8], [9,10,11,12],[13,14,15,16]]
row = []
column = [] 
length = len(data)
for i in range(length):
	for j in range(length):
		if data[i][j] == 0:
			row.append(i)
			column.append(j)

for i in row:
	for j in range(length):
		data[i][j] = 0
for i in column:
	for j in range(length):
		data[j][i] = 0

print data