class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        res = []
        dictionary = {}
        upt_grid = []
        for i in grid:
            for j in i:
                upt_grid.append(j)
        for i in upt_grid:
            dictionary[i] = 1 + dictionary.get(i, 0)
        for key, val in dictionary.items():
            if val > 1:
                res.append(key)
                break
        nums = [i for i in range(1, len(grid)*len(grid)+1)]
        sum_nums = sum(nums)
        repeated = False
        for i in upt_grid:
            if not repeated and res[0] == i:
                repeated = True
            else:
                sum_nums -= i
        res.append(sum_nums)
        return res
