class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        unordered_set<string> operators = {"+", "-", "*", "/"};
      
        for (const string& token : tokens) {
            if (!operators.contains(token)) {
                st.push(stoi(token));
            } else {
                int right_operand = st.top();
                st.pop();
                int left_operand = st.top();
                st.pop();

                switch (token[0]) {
                    case '+':
                        st.push(left_operand + right_operand);
                        break;
                    case '-':
                        st.push(left_operand - right_operand);
                        break;
                    case '*':
                        st.push(left_operand * right_operand);
                        break;
                    case '/':
                        st.push(left_operand / right_operand);
                        break;
                }
            }
        }

        return st.top();
    }
};
