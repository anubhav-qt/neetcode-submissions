class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> num_set(nums.begin(), nums.end());
        int lcs{0};
        
        for (const int& num: num_set) {
            if (!num_set.count(num - 1)) {
                int curr_length{1}, n{num};
                while (num_set.count(++n)) ++curr_length;
                lcs = max(lcs, curr_length);
            }
        }

        return lcs;
    }
};
