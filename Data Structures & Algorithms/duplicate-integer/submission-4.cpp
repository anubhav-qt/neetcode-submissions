# include <unordered_set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> visited;
        for (auto num: nums) {
            if (visited.count(num)) return true;
            visited.insert(num);
        } return false;
    }
};