class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        greatest = 0
        for i in accounts:
            count = 0
            for j in i:
                count += j
            if count > greatest:
                greatest = count
        return greatest
