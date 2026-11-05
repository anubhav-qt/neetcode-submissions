// simple algorithm to find if the same characters (regardless of order) are present in the two strings
// algorithm:
// initialize 2 arrays of integers of length 26, all 0s
// add both arrays with strings s and t's respective frequencies in the respective indices
// compare the two arrays
// if same return true else false

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        vector<int> freq_s(26, 0), freq_t(26, 0);

        for (int i = 0; i < s.size(); ++i) {
            ++freq_s[s[i] - 'a'];
            ++freq_t[t[i] - 'a'];
        }

        return (freq_s == freq_t);
    }
};
