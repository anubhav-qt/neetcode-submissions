#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> value_index_map;
        std::vector<int> res(2, -1);
        for (int i = 0; i < nums.size(); ++i) {
            if ((value_index_map.count((target - nums[i]))) && (i != value_index_map[(target - nums[i])])){
                res[0] = std::min(i, value_index_map[(target - nums[i])]);
                res[1] = std::max(i, value_index_map[(target - nums[i])]);
                return res;
            }

            value_index_map[nums[i]] = i;
        }
    }
};
