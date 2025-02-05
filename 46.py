class Solution(object):
    def permute(self, nums):
        def backtrack(start, path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(i+1, path)
                    path.pop()
        result = []
        backtrack(0, [])
        return result
