vector<int> findDisappearedNumbers(vector<int>& nums) {
        std::vector<int> result;
        for(int i = 1; i < nums.size() + 1; i++)
        {
            if(std::find(nums.begin(), nums.end(), i) == nums.end())
            {
                result.push_back(i);
            }
        } 
        return result;
    }
