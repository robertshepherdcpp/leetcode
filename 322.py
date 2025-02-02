class Solution(object):
    def coinChange(self, coins, amount):
        counts = []
        for i in range(len(coins)):
            for j in range(len(coins)):
                if i != j:
                    counts.append(coins[i] + coins[j])
                elif i == j:
                    counts.append(coins[i])
        counts = sorted(counts)
        total = amount
        count = 0
        for i in counts[::-1]:
            if total / i >= 1:
                # i does fit into current amount
                count += (total - (total % i)) / i
                total = total % i
            if total == 0:
                return count
        return -1
