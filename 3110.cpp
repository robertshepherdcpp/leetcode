class Solution {
public:
    int scoreOfString(string s) {
        int count = 0;
        for(int i = 1; i < s.size(); i++)
        {
            count += std::abs(int(s[i - 1]) - int(s[i]));
        }
        return count;
    }
};
