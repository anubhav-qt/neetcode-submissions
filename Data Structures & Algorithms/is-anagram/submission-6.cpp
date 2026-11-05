#include <vector>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        std::vector<int> count_s(26, 0);
        std::vector<int> count_t(26, 0);
        
        for (int i = 0; i < s.size(); ++i) {
            ++count_s[s[i] - 'a'];
            ++count_t[t[i] - 'a'];
        }

        return (count_s == count_t);
    }
};
