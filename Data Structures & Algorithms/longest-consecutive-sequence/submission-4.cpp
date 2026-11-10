// one way is to sort, but that is O(n log n)
// another way: hash map

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int size {0}, max_size {0}, current_element {0};
        unordered_set<int> seen;

        for (const auto& num : nums) {
            seen.insert(num);
        }

        for (const auto& num : seen) {
            current_element = num;
            size = 1;
            while (seen.contains(--current_element)) {
                seen.erase(current_element);
                ++size;
            }

            current_element = num;
            while (seen.contains(++current_element)) {
                seen.erase(current_element);
                ++size;
            }

            max_size = max(size, max_size);
        }

        return max_size;
    }
};
