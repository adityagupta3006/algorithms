def isUnique(data):
    d = dict()
    for i in data:
        if i not in d:
            d[i] = 1
        else:
            return "false"
    return "true"


string = "adityagupta"
out = isUnique(string)
print out