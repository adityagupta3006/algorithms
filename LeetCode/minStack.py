class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        min = self.getMin()
        if min==None or x<min:
            min = x
        self.stack.append((x, min))
        
    def pop(self):
        return self.stack.pop()
        

    def top(self):
        return self.stack[-1][0]
        

    def getMin(self):
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack)-1][1]
        
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()