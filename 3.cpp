auto contains_duplicates(std::string s) -> bool
{
    std::vector<char> previous{};
    for (const auto& x : s)
    {
        if (std::find(previous.begin(), previous.end(), x) == std::end(previous))
        {
            previous.push_back(x);
        }
        else
        {
            return true;
        }
    }
    return false;
}

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 0)
        {
            return 0;
        }
        std::string longest_substring = std::string{ s[0] };
        for (int i = 0; i <= s.size(); i++)
        {
            for (int j = 0; j <= s.size(); j++)
            {
                if (!contains_duplicates(s.substr(i, j)) && s.substr(i, j).size() > longest_substring.size())
                {
                    longest_substring = s.substr(i, j);
                }
            }
        }
        if (longest_substring == std::string{ s[0] } &&
            std::find(s.begin() + 1, s.end(), s[0]) == std::end(s))
        {
            return s.size();
        }
        else
        {
            return longest_substring.size();
        }
    }
};