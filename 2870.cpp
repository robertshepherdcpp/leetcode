auto count_appearances(int a, std::vector<int>& y)
{
    int count = 0;
    for (const auto& x : y)
    {
        if (x == a) { count += 1; }
        else {/*do nothing*/ }
    }
    return count;
}

auto get_all_appearances(int a, std::vector<int>& y)
{
    std::vector<int> result{};
    for (const auto& x : y)
    {
        if (x == a)
        {
            result.push_back(x);
        }
        else {/*do nothing*/ }
    }
    return result;
}

auto find_in_vec(int a, std::vector<int>& y)
{
    for (int i = 0; i < y.size(); i++)
    {
        if (y[i] == a)
        {
            return i;
        }
    }
    return -1;
}

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        // we first have to check if there are a multiple of 2 or 3 of a certain number
        for (const auto& x : nums)
        {
            int num = x;
            if (find_in_vec(num, has_been_checked) == -1)
            {
                has_been_checked.push_back(num);
                if (count_appearances(num, nums) % 2 == 0 ||
                    count_appearances(num, nums) % 3 == 0)
                {
                    // we dont return -1, this is a valid sequence in the array.
                    // find all occurences in the vector of the good number and then
                    // push that back into valid_numbers.
                    valid_numbers.push_back(num);
                }
                else
                {
                    return -1;
                }
            }
        }
        // so we know that is true that it is possible because no -1 has been returned.
        // we got to this moment in code without returning, all nums fine
        int amount_of_moves = 0;
        has_been_checked = {};
        for (const auto& x : valid_numbers)
        {

            int appearances = count_appearances(x, nums);
            for (int i = 0; i < nums.size(); i++)
            {
                if (appearances > 1)
                {
                    int remainder_three = appearances % 3;
                    int divide_three = (appearances - remainder_three) / 3;
                    amount_of_moves += divide_three;
                    appearances -= (divide_three * 3);

                    int remainder_two = appearances % 2;
                    int divide_two = (appearances - remainder_two) / 2;
                    amount_of_moves += divide_two;
                    appearances -= (divide_two * 2);
                }
            }
        }
        return amount_of_moves;
    }

    std::vector<int> has_been_checked{};
    std::vector<int> valid_numbers{};
};