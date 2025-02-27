class Solution(object):
    def lenLongestFibSubseq(self, arr):
        # do a two sum
        def find_sub(arr, to_find):
            for sub_arr in range(len(arr)):
                if arr[sub_arr][:2] == to_find:
                    return sub_arr
            return None
        array = []
        dictionary = {}
        # i is target value
        for i in range(len(arr)):
            dictionary[arr[i]] = i
        for i in range(len(arr)):
            # j is index in array
            for j in range(len(arr)):
                if (i != j and (arr[i] - arr[j]) in dictionary):
                    corresponding = dictionary[arr[i] - arr[j]]
                    # array[i].append([j, corresponding])
                    if j != corresponding:
                        if arr[j] < arr[corresponding]:
                            array.append([j, corresponding, i])
                        else:
                            array.append([corresponding, j, i])
        # now we got at each index which values add up to it,
        # so we need to match up
        max_len = -1
        for i in range(len(array)):
            curr = array[i][1:]
            # all_vals = [i for i in array[i][:2]]
            all_vals = set()
            for i in array[i][:2]:
                all_vals.add(i)
            while find_sub(array, curr) != None:
                if curr[-1] not in all_vals:
                    all_vals.add(curr[-1])
                idx = find_sub(array, curr)
                curr = array[idx][1:]
            max_len = max(max_len, len(all_vals))
        return max_len + 1
        
                
        
