class Solution {
public:
    void backtrack(int start, int sum, int target, vector<int>& combination, vector<vector<int>>& res, vector<int>& nums) {
        if (sum == target) {
            res.push_back(combination);
            return;
        }
        if (sum > target) return;

        for (int i = start; i < nums.size(); ++i) {
            combination.push_back(nums[i]);
            backtrack(i, sum + nums[i], target, combination, res, nums);
            combination.pop_back();
        }
    }
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        vector<int> combination;
        backtrack(0, 0, target, combination, res, nums);
        return res;
    }
};
