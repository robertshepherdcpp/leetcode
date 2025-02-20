class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for i in magazine:
            if i in ransomNote:
                idx = ransomNote.index(i)
                ransomNote = ransomNote[:idx] + ransomNote[idx+1:]
        return len(ransomNote) == 0
        
