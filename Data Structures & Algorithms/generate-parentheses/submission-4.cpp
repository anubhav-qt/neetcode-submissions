class Solution {
public:
    void backtrack(int count_open, int count_closed, int n, vector<string>& res, string& stack) {
        if (count_open == count_closed && count_open == n) {
            res.push_back(stack);
            return;
        }

        if (count_open < n) {
            stack.push_back('(');
            backtrack(count_open + 1, count_closed, n, res, stack);
            stack.pop_back();
        }

        if (count_closed < count_open) {
            stack.push_back(')');
            backtrack(count_open, count_closed + 1, n, res, stack);
            stack.pop_back();
        }
    }

    vector<string> generateParenthesis(int n) { 
        vector<string> res;
        string stack;
        backtrack(0, 0, n, res, stack);
        return res;
    }
};
