class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        if len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) == 1 and nums[0] != target:
            return -1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # so then we want the right side
                left = mid + 1
            elif nums[mid] > target:
                # so we want the left side
                right = mid - 1
        if nums[left] == target:
            return left
        else:
            return -1
        
