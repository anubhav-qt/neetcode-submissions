class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        int left_operand, right_operand;
        unordered_set<string> operators = {"+", "-", "*", "/"};
      
        for (const string& token : tokens) {
            if (!operators.contains(token)) {
                st.push(stoi(token));
            } else {
                right_operand = st.top();
                st.pop();
                left_operand = st.top();
                st.pop();

                if (token == "+") st.push(left_operand + right_operand);
                else if (token == "-") st.push(left_operand - right_operand);
                else if (token == "*") st.push(left_operand * right_operand);
                else st.push(left_operand / right_operand);
            }
        }

        return st.top();
    }
};
