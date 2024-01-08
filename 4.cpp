class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        for (const auto x : nums2)
        {
            nums1.push_back(x);
        }
        // now we have the merged array.
        std::sort(nums1.begin(), nums1.end());
        // now it is a sorted array
        if (nums1.size() % 2 == 0)
        {
            double first_num = nums1[(nums1.size() / 2) - 1];
            double second_num = nums1[(nums1.size() / 2)];
            return (first_num + second_num) / 2.0;
        }
        else
        {
            return nums1[((nums1.size() + 1) / 2.0) - 1];
        }
    }
};