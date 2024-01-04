auto equal(const std::string& a, const std::string& b)
{
    return a == b;
}

auto reverse(const std::string& s)
{
    std::string result{};
    for (int i = s.size() - 1; i >= 0; i--)
    {
        result.append(std::string{ s[i] });
    }
    return result;
}

class Solution {
public:
    bool isPalindrome(int x) {
        return equal(reverse(std::to_string(x)), std::to_string(x));
    }
};