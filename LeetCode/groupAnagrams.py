import collections
def anagrams(data):
	d = collections.defaultdict(list)

	for i in data:
		d[tuple(sorted(i))].append(i)
	return list(d.values())
data = ["eat", "tea", "tan", "ate", "nat", "bat"]
print (anagrams(data))