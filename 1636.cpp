class Solution {
public:
    vector<int> vecTimes(int num, int times)
    {
        return std::vector<int>(num, times);
    }
    vector<int> frequencySort(vector<int>& nums) {
        std::map<int, int> m{};
        for(auto x : nums)
        {
            m[x] += 1;
        }
        std::vector<std::pair<int, int>> pairs{};
        for (const auto& [key, value] : m)
        {
            pairs.push_back(std::pair<int, int>{key, value});
        }
        std::sort(pairs.begin(), pairs.end(), [](std::pair<int, int>& a, std::pair<int, int>& b)
        {
            //return a.second < b.second;
            if(a.second == b.second)
            {
                return true;
            }
            else {
                return a.second < b.second;
            }
        });
        // now we have the sorted version, so we just now need to use the first value
        // and then put it in a vector.
        std::vector<int> result{};
        for(auto x : pairs)
        {
            auto vec = std::vector<int>(x.second, x.first);
            for(auto y : vec)
            {
                result.push_back(y);
            }
        }
        return result;
    }
};
