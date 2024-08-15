class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        current = []
        for i in bills:
            if i == 5:
                current.append(i)
            if i == 10:
                if 5 in current:
                    current.pop(current.index(5))
                    current.append(i)
                else:
                    return False
            if i == 20:
                if 10 in current and 5 in current:
                    current.pop(current.index(5))
                    current.pop(current.index(10))
                    current.append(i)
                elif current.count(5) >= 3:
                    current.pop(current.index(5))
                    current.pop(current.index(5))
                    current.pop(current.index(5))
                    current.append(i)
                else:
                    return False
        return True
