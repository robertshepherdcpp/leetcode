// leetcode passes 84 tests but when I should return an empty string, it says i return: "" with a block in the middle
// but it doesn't appear in this ide, but to my knowledge it works to the other test cases that don't involve the "".

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0 || strs.empty())
        {
            return "";
        }

        int current_index = 0;
        std::string current_prefix{ std::string{strs[0][0]} };
        for (int i = 0; i < strs[0].size(); i++)
        {
            for (int j = 0; j < strs.size(); j++)
            {
                if (strs[j].find(current_prefix) != -1)
                {
                    if (j == (strs.size() - 1))
                    {
                        current_index += 1;
                        current_prefix = strs[0].substr(0, current_index);
                    }
                }
                else
                {
                    if (current_index == 0)
                    {
                        return ""; // because there is no common prefix.
                    }
                    else
                    {
                        if (current_index > 1)
                        {
                            return current_prefix.substr(0, current_index - 1);
                        }
                        else
                        {
                            return "";
                        }
                    }
                }
            }
        }
        return current_prefix;
    }
};