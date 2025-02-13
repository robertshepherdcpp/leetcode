class MinStack(object):

    def __init__(self):
        self.arr = []

    def push(self, val):
        if self.arr:
            minimum = min(val, self.arr[-1][1])
        else:
            minimum = val
        self.arr.append([val, minimum])

    def pop(self):
        self.arr = self.arr[:len(self.arr) - 1]
        

    def top(self):
        return self.arr[-1][0]
        

    def getMin(self):
        return self.arr[-1][1]
        
