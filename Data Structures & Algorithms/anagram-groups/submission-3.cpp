class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> map;
        for (auto str: strs) {
            std::vector<int> count(26, 0);
            for (auto c: str) {
                count[c - 'a'] += 1;
            }
            
            std::string count_str = "";
            for (int i = 0; i < 26; ++i) {
                count_str += to_string(count[i]) + '#';
            }
            map[count_str].push_back(str);
        }

        std::vector<std::vector<std::string>> res;
        for (const auto& pair: map) {
            res.push_back(pair.second);
        }
        return res;
    }
};
