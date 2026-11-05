// algorithm to return an array of arrays of anagrams
// algorithm:
// initialize an array of int, size 26, all 0s named freq
// initialize a hash map of string (for freq, but with a separator to make it a string) as key and the array of strings of that freq as values named output
// for each string in strs, freq is initially cleared to all 0s -- O(mn)
// freq is filled for the string
// freq is hashed with a separator
// output's freq key gets appended with the current freq's value string
// return output as an array

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        array<int, 26> freq;
        unordered_map<string, vector<string>> output_map;

        for (const auto& str : strs) {
            freq.fill(0);
            for (char c : str) {
                ++freq[c - 'a'];
            }

            string hashed_freq;
            for (int i = 0; i < 26; ++i) {
                hashed_freq += to_string(freq[i]) + '#';
            }

            output_map[hashed_freq].push_back(str);
        }

        vector<vector<string>> output;
        output.reserve(output_map.size());

        for (auto& [key, value] : output_map) {
            output.push_back(move(value));
        }
        
        return output;
    }
};
