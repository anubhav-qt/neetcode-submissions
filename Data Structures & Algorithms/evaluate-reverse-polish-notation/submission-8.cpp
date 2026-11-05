class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> stack; // stores the operands until we get an operator
        for (const string& c: tokens) {
            if (c == "+" || c == "-" || c == "*" || c == "/") {
                // take the last two element
                int second = stack[stack.size() - 1], first = stack[stack.size() - 2];
                stack.pop_back();
                stack.pop_back();

                // perform the operation and push it back onto the stack
                if (c == "+") stack.push_back(first + second);
                else if (c == "-") stack.push_back(first - second);
                else if (c == "*") stack.push_back(first * second);
                else stack.push_back(first / second);
            } else {
                stack.push_back(stoi(c));
            }
        }

        return stack[0];
    }
};
