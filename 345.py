class Solution(object):
    def reverseVowels(self, s):
        indexes = []
        s_list = list(s)
        for i in range(len(s)):
            if str(s[i]).lower() in "aeiou":
                indexes.append(i)
        copy_str = s
        indexes_copy = indexes[::-1]
        for i in range(len(indexes)):
            s_list[indexes[i]] = copy_str[indexes_copy[i]]
        return ''.join(i for i in s_list)

        
