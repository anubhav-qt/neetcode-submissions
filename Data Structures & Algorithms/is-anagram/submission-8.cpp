// simple algorithm to find if the same characters (regardless of order) are present in the two strings
// algorithm:
// initialize 2 arrays of integers of length 26, all 0s
// add both arrays with strings s and t's respective frequencies in the respective indices
// compare the two arrays
// if same return true else false

class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> freq_s(26, 0), freq_t(26, 0);

        for (char c : s) {
            int index = c - 'a';
            ++freq_s[index];
        }

        for (char c : t) {
            int index = c - 'a';
            ++freq_t[index];
        }

        return (freq_s == freq_t);
    }
};
