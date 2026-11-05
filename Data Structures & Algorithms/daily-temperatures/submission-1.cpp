class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<pair<int, int>> stack;
        vector<int> output(temperatures.size());

        for (int i = 0; i < temperatures.size(); ++i) {
            if (stack.empty()) {
                stack.push_back({temperatures[i], i});
            } else {
                while (!stack.empty() && stack[stack.size() - 1].first < temperatures[i]) {
                    output[stack[stack.size() - 1].second] = i - stack[stack.size() - 1].second;
                    stack.pop_back();
                }
                stack.push_back({temperatures[i], i});
            }
        }

        return output;
    }
};
