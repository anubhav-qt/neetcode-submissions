class Solution {
public:
    void backtrack(int start, vector<int>& temp, vector<vector<int>>& res, vector<int>& nums) {
        res.push_back(temp);
        for (int i = start; i < nums.size(); ++i) {
            temp.push_back(nums[i]);
            backtrack(i + 1, temp, res, nums);
            temp.pop_back();
        }
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> temp;
        vector<vector<int>> res;
        backtrack(0, temp, res, nums);
        return res;
    }
};
