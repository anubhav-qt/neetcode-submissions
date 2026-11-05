class Solution {
public:

    string encode(vector<string>& strs) {
        string res;
        for (const auto& str: strs) {
            res += to_string(str.size()) + '#' + str;
        } return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        for (int i = 0; i < s.size(); ++i) {
            string temp_count;
            while (s[i] != '#') temp_count += s[i++];

            int count = stoi(temp_count);
            string temp_str;
            for (int k = 0; k < count; ++k) {
                temp_str += s[++i];
            } res.push_back(temp_str);
        }

        return res;
    }
};
