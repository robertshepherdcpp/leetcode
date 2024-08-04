class Solution {
public:
    int rangeSum(vector<int>& nums, int n, int left, int right) {
        std::vector<int> sub_array_sums{};
        // first get all of the subarrays sums.
        for(int i = 0; i < nums.size(); i++)
        {
            for(int j = 0; j < nums.size(); j++)
            {
                if(i != j && i < j)
                {
                    // now we need to get the subarray from i to j
                    std::vector<int> subarray{};
                    for(int x = i; x <= j; x++)
                    {
                        subarray.push_back(nums[i]);
                    }
                    // after we have got the subarray, we now need to get the sum.
                    int sum = std::accumulate(subarray.begin(), subarray.end(), 0);
                    sub_array_sums.push_back(sum);
                }
            }
        }
        // now we have got the sums. we need to sort them in decreasing order.
        std::sort(sub_array_sums.begin(), sub_array_sums.end(), [](int a, int b){return a < b;});
        // now it is sorted, so we need to get the sum of the elements from left to right.
        int final_sum{0};
        for(int x = left - 1; x < right; x++)
        {
            final_sum += sub_array_sums[x];
        }
        return final_sum;
    }
};
