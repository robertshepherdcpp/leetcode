class Solution {
public:
    int romanToInt(string s)
    {
        int total = 0;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == 'I')
            {
                total += 1;
            }
            if (s[i] == 'V')
            {
                if ((i - 1) >= 0 && s[i - 1] == 'I')
                {
                    total += 3;
                }
                else
                {
                    total += 5;
                }
            }
            if (s[i] == 'X')
            {
                if ((i - 1) >= 0 && s[i - 1] == 'I')
                {
                    total += 8;
                }
                else
                {
                    total += 10;
                }
            }
            if (s[i] == 'L')
            {
                if ((i - 1) >= 0 && s[i - 1] == 'X')
                {
                    total += 30;
                }
                else
                {
                    total += 50;
                }
            }
            if (s[i] == 'C')
            {
                if ((i - 1) >= 0 && s[i - 1] == 'X')
                {
                    total += 80;
                }
                else
                {
                    total += 100;
                }
            }
            if (s[i] == 'D')
            {
                if ((i - 1) >= 0 && s[i - 1] == 'C')
                {
                    total += 300;
                }
                else
                {
                    total += 500;
                }
            }
            if (s[i] == 'M')
            {
                if ((i - 1) >= 0 && s[i - 1] == 'C')
                {
                    total += 800;
                }
                else
                {
                    total += 1000;
                }
            }
        }
        return total;
    }
};