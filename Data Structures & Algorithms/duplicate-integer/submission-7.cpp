// simple algorithm returning true if contain duplicate else false
// hash map or sorting works, we try doing faster and not thinking much of space so we do hash map
// algorithm:
// declare hash set seen of int
// loop through nums, check each number if in seen, return true else add in seen
// after loop return flase

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;

        for (const int& n : nums) {
            if (seen.contains(n)) {
                return true;
            } else {
                seen.insert(n);
            }
        }

        return false;
    }
};