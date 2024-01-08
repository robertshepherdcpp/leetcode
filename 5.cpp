// this takes too long, but this still works when the text is not too large.

string reverseString(std::string x)
{
    std::string s{};
    for (int i = x.size() - 1; i >= 0; i--)
    {
        s.append(std::string{ x[i] });
    }
    return s;
}

bool isPalindrome(std::string s)
{
    return (s == (reverseString(s)));
}

class Solution {
public:
    string longestPalindrome(string s) {
        if (s.size() == 1)
        {
            return s;
        }
        std::string current_longest{};
        for (int i = 0; i <= s.size(); i++)
        {
            for (int j = 0; j <= s.size(); j++)
            {
                if (isPalindrome(s.substr(i, j)) && (s.substr(i, j).size() > current_longest.size()))
                {
                    current_longest = s.substr(i, j);
                }
            }
        }
        return current_longest;
    }
};