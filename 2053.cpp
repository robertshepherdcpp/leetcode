class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        std::map<std::string, int> occurances {};
        int count = 0;
        for(auto x : arr)
        {
            occurances[x]++;
        }
        for (const auto& [key, value] : occurances)
        {
            if(value == 1 && (count + 1) == k)
            {
                return key;
            }
            count++;
        }
        return {};
    }
};
