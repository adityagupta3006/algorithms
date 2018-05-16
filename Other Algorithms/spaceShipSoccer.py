from operator import itemgetter

numberOfIterations = int(input())
time = []
for i in range(numberOfIterations):
    a = input().split(' ')
    time.append((int(a[1]), int(a[0]), int(a[2])))

time = sorted(time, key=itemgetter(0), reverse = True)    

result = []

result.append((time[0][1], 0))

for i in range(1, numberOfIterations):
    rank = 0
    #count = 0
    endTime = time[i][2]
    for j in range(i):
        currEndTime = time[j][2]
        if endTime > currEndTime:
            rank += 1
    result.append((time[i][1], rank))
result = sorted(result, key=itemgetter(1, 0))
for i in result:
    print(i[0], i[1])