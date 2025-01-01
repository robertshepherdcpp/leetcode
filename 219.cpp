auto find_not_index(std::vector<int>& v, int index, int to_find)
{
    for(int i = 0; i < v.size(); i++)
    {
        if(index != i && to_find == v[i])
        {
            return i;
        }
    }
    return -1;
}

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        std::map<int, int> counts{};
        for(auto x : nums)
        {
            if(counts.find(x) != counts.end())
            {
                counts[x]++;
            }
            else {
                counts[x] = 1;
            }
        }

        // [1, 2]
        // once we have counts, we need to go through all the counts.
        for(int i = 0; i < nums.size(); i++)
        {
            // 0
            if(counts[nums[i]] > 1)
            {
                if(std::abs(i - find_not_index(nums, i, nums[i])) == k)
                {
                    return true;
                }
            }
        }

        return false;
    }
};
