class Solution(object):
    def buildArray(self, target, n):
        iota = []
        for i in range(n, 0, -1):
            iota.append(i)
        res = []
        moves = []
        while res != target:
            res.append(iota.pop())
            moves.append("Push")
            print(res, target[:len(res)])
            if res != target[:len(res)]:
                res.pop()
                moves.append("Pop")
        return moves
        
        
