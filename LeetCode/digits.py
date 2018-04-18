class Solution(object):
    def letterCombinations(self, digits):
        d = {'2': 'abc', '3': 'def', "4": 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        l = len(digits)
        output = [''] if digits else []
        
        
        for digit in digits:
            current_combinations = []
            for letter in d[digit]:
                for o in output:
                    current_combinations.append(o + letter)
            output = current_combinations
        return output