class Solution(object):
    def numIslands(self, grid):
        idxs = set([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    idxs.add((i,j))
        if len(idxs) == 0:
            return 0
        stack = []
        count = 0
        while idxs:
            stack.append(idxs.pop())
            count += 1
            while stack:
                idx = stack.pop()
                if idx[0] > 0:
                    if (idx[0]-1, idx[1]) in idxs:
                        idxs.remove((idx[0]-1,idx[1]))
                        stack.append([idx[0]-1,idx[1]])
                if idx[0] < (len(grid)-1):
                    if (idx[0]+1, idx[1]) in idxs:
                        idxs.remove((idx[0]+1,idx[1]))
                        stack.append([idx[0]+1,idx[1]])
                if idx[1] > 0:
                    if (idx[0], idx[1]-1) in idxs:
                        idxs.remove((idx[0], idx[1]-1))
                        stack.append([idx[0], idx[1]-1])
                if idx[1] < len(grid[0])-1:
                    if (idx[0], idx[1]+1) in idxs:
                        idxs.remove((idx[0], idx[1]+1))
                        stack.append([idx[0], idx[1]+1])
        return count
        
