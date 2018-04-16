def solution(S):
    minutes = (S[3:5])
    hours = (S[0:2])
    maxHour = 23
    maxMinute = 59
    time = (hours+minutes)
    permutations = findPermutations(time) 
    permutations = [x for x in permutations if int(x[:2])<24 and int(x[2:4])<60]
    permutations = list(set(permutations)) # getting unique permutations
    
    permutations.sort()
    i = permutations.index(time) # index of current time
    permLen =len(permutations)
    if permLen != 1 and (permLen-1) != i:
        result = permutations[i+1] 
    else:
        result = permutations[0]
                
    print result[:2] + ':' + result[2:4] 

def findPermutations(data):
    l = len(data)
    if l == 0:
        return ''

    if l == 1:
        return data
    
    permutations = []
    for i in range(l):
        static = data[i]
        rest = data[:i] + data[i+1:]
        #print rest
        for p in findPermutations(rest):
            permutations.append(static + p)
    return permutations
time = "12:34"
solution(time)