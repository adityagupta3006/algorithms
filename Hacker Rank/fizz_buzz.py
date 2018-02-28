class Solution(object):
    def fizzBuzz(self, n):
        array = []
        for a in range(1,n+1):
            if a%15 == 0:
                array.append(str("FizzBuzz"))
            elif a%3 == 0:
                array.append(str("Fizz"))
            elif a%5 == 0:
                array.append(str("Buzz"))
            else:
                array.append(str(a))
        return(array)
