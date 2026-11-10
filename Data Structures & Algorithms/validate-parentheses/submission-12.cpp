class Solution {
public:
    bool isValid(string s) {
        stack<int> p_stack;
        unordered_set<char> open_parenthesis = {'[', '{', '('};

        for (char c : s) {
            if (open_parenthesis.contains(c)) p_stack.push(c);

            else if (p_stack.size() == 0) p_stack.push(c);
            
            else if (c == ']') {
                if (p_stack.top() == '[') p_stack.pop();
                else p_stack.push(c);
            }
            
            else if (c == '}') {
                if (p_stack.top() == '{') p_stack.pop();
                else p_stack.push(c);
            }

            else if (c == ')') {
                if (p_stack.top() == '(') p_stack.pop();
                else p_stack.push(c);
            }
        }

        if (p_stack.size() != 0) return false;
        else return true;
    }
};
