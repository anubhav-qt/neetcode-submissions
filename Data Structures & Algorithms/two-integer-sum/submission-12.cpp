// algorithm to return indices of the numbers which sum to target
// algorithm:
// initialize output array of size 2
// initialize hash map seen of int, int containing number and its index
// for each num in nums, if in seen return the output with current num's index and seen nums index

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); ++i) {
            if (seen.contains(target - nums[i])) return {seen[target - nums[i]], i};
            seen[nums[i]] = i;
        }

        return {0, 0};
    }
};
