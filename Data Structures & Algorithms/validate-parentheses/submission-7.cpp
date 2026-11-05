class Solution {
public:
    bool isValid(string s) {
        if (s.size() == 1) return false;
        vector<int> stack;
        string open = "[{(";
        for (const char& c: s) {
            if (open.find(c) != string::npos) stack.push_back(c);
            else if (c == ']') {
                if ((!stack.empty()) && stack[stack.size() - 1] == '[') stack.pop_back();
                else return false;
            } else if (c == '}') {
                if ((!stack.empty()) && stack[stack.size() - 1] == '{') stack.pop_back();
                else return false;
            } else {
                if ((!stack.empty()) && stack[stack.size() - 1] == '(') stack.pop_back();
                else return false;
            }
        }

        return stack.empty();
    }
};
