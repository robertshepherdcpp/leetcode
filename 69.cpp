class Solution {
public:
    int mySqrt(int x) {
        std::string number = std::to_string(sqrt(x));
        int pos_of_decimal = -1;
        for (int i = 0; i < number.size(); i++)
        {
            if (number[i] == '.' && pos_of_decimal == -1)
            {
                pos_of_decimal = i;
            }
        }
        if (pos_of_decimal == -1)
        {
            return sqrt(x);
        }
        else
        {
            return std::stoi(number.substr(0, pos_of_decimal));
        }
    }
};