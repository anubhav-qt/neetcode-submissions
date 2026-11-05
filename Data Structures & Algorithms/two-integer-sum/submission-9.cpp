#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> value_index_map;
        for (int i = 0; i < nums.size(); ++i) {
            if ((value_index_map.count((target - nums[i])))) return {value_index_map[target - nums[i]], i};
            value_index_map[nums[i]] = i;
        }
    }
};
