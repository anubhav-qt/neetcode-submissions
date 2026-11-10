class Solution {
public:
    bool isValid(string s) {
        stack<char> p_stack;
        unordered_set<char> open_parenthesis = {'[', '{', '('};

        for (char c : s) {
            if (open_parenthesis.contains(c)) p_stack.push(c);

            else if (p_stack.size() == 0) return false;
            
            else if (c == ']') {
                if (p_stack.top() == '[') p_stack.pop();
                else return false;
            }
            
            else if (c == '}') {
                if (p_stack.top() == '{') p_stack.pop();
                else return false;
            }

            else if (c == ')') {
                if (p_stack.top() == '(') p_stack.pop();
                else return false;
            }
        }

        return p_stack.empty();
    }
};
