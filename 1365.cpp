vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        std::vector<int> ans{};
        for(int i = 0; i < nums.size(); i++)
        {
            int curr = 0;
            for(int j = 0; j < nums.size(); j++)
            {
                if(nums[i] > nums[j])
                {
                    curr += 1;
                }
            }
            ans.push_back(curr);
        }
        return ans;
    }
