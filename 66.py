class Solution(object):
    def plusOne(self, digits):
        if digits[-1] == 9:
            if len(digits) == 1:
                return [1, 0]
            curr = -1
            while digits[curr-1] == 9 and abs(curr-1) != len(digits):
                curr -= 1
            print(curr)
            if abs(curr) == len(digits):
                return [1] + [0] * len(digits)
            else:
                same = digits[:curr-1]
                same += [digits[curr-1] + 1]
                same += [0] * (abs(curr))
                if same[0] == 10:
                    same = [1,0] + same[1:]
                return same
        else:
            digits[-1] = digits[-1]+1
            if digits[0] == 10:
                digits = [1,0] + digits[1:]
            return digits
