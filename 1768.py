class Solution(object):
    def mergeAlternately(self, word1, word2):
        string = ''.join(i for i in [element for sub in zip(word1, word2) for element in sub])
        if len(word1) < len(word2):
            string += word2[len(word1):]
        elif len(word1) > len(word2):
            string += word1[len(word2):]
        return string
        
