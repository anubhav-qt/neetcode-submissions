class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> st;
        vector<int> output(temperatures.size(), 0);

        for (int i = 0; i < temperatures.size(); ++i) {
            while (!st.empty() && st.top().first < temperatures[i]) {
                output[st.top().second] = i - st.top().second;
                st.pop();
            }
            
            st.push({temperatures[i], i});
        }

        while (!st.empty()) {
            output[st.top().second] = 0;
            st.pop();
        }

        return output;
    }
};
