class Solution(object):
    def minimumAbsDifference(self, arr):
        diffs = []
        arr = sorted(arr)
        for i in range(1, len(arr)):
            diffs.append(abs(arr[i] - arr[i - 1]))
        absd = min(diffs)
        nums = []


        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == absd:
                nums.append([arr[i - 1], arr[i]])
        return nums
