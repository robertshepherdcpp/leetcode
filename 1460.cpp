class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        if((target.size() == 1) && (target[0] == arr[0])) return true;
        // check if there are any differences in numbers, e.g.:
        //      3 7 9    , 2 7 11
        std::vector<std::pair<int, bool>> vals_there{}; // not using map, maybe duplicates
        for(auto x : target) 
        {
            vals_there.push_back(std::pair<int, bool>{x, false});
        }
        // now we go through every one of the other elements, and then tick them off accordingly
        for(auto y : arr)
        {
            auto it = std::find(vals_there.begin(), vals_there.end(), std::pair<int, bool>{y, false});
            if(it != std::end(vals_there))
            {
                it->second = true;
            }
            else
            {
                return false;
            }
        }
        return true;
    }
};
