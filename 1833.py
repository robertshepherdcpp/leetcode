class Solution(object):
    def maxIceCream(self, costs, coins):
        max_num = max(costs)
        countArr = [0]*(max_num+1)
        output = [0] * len(costs)
        for i in costs:
            countArr[i] += 1
        for i in range(1, max_num+1):
            countArr[i] += countArr[i-1]
        for i in range(len(costs)-1, -1, -1):
            output[countArr[costs[i]]-1] = costs[i]
            countArr[costs[i]] -= 1
        count = 0
        total = 0
        print(output)
        for i in output:
            if total + i <= coins:
                count += 1
                total += i
            else:
                break
        return count
        
