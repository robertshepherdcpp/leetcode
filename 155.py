class MinStack(object):

    def __init__(self):
        self.arr = []

    def push(self, val):
        self.arr.append(val)
        

    def pop(self):
        self.arr = self.arr[:len(self.arr) - 1]
        

    def top(self):
        return self.arr[-1]
        

    def getMin(self):
        return min(self.arr)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
