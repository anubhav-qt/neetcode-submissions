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
        vector<int> freq(26, 0);

        for (int i = 0; i < s.size(); ++i) {
            ++freq[s[i] - 'a'];
            --freq[t[i] - 'a'];
        }

        for (int element : freq)
            if (element != 0) return false;
        
        return true;
    }
};
