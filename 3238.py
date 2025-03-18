class Solution(object):
    def winningPlayerCount(self, n, pick):
        dictionary = {}
        count = 0
        for i in pick:
            value = i[0]
            dictionary[value] = dictionary.get(value, []) + [i[1]]
        for key, val in dictionary.items():
            hashmap = {}
            for i in val:
                hashmap[i] = hashmap.get(i, 0) + 1
            for i in hashmap.values():
                if i > key:
                    count += 1
                    break
        return count
