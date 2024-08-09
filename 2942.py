class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indexes = []
        for i in range(0, len(words)):
            if(words[i].count(x) > 0):
                indexes.append(i)
        return indexes
