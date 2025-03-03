class Solution():
    def pivotArray(self, nums, pivot):
        before = []
        after = []
        mid = []
        for i in nums:
            if i < pivot:
                before.append(i)
            elif i == pivot:
                mid.append(i)
            elif i > pivot:
                after.append(i)
        return before + mid + after
