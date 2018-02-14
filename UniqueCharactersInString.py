'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

'''
def isUnique(word):
        dictionary = {}
        for a in word:
                if(a in dictionary):
                        return False
                dictionary[a] = 1
        return True

string_input = raw_input('enter the input: ') 
print isUnique(string_input)
raw_input("Press any key")