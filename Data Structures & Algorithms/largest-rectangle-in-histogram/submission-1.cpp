class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> st;
        vector<int> left(heights.size(), -1), right(heights.size(), -1);
        int max_area {0};

        for (int i = 0; i < heights.size(); ++i) {
            while (!st.empty() && heights[st.top()] >= heights[i]) {
                st.pop();
            }

            left[i] = st.empty() ? -1 : st.top();
            st.push(i);
        }

        while (!st.empty()) st.pop();

        for (int i = heights.size() - 1; i >= 0; --i) {
            while (!st.empty() && heights[st.top()] >= heights[i]) {
                st.pop();
            }

            right[i] = st.empty() ? heights.size() : st.top();
            st.push(i);
        }

        for (int i = 0; i < heights.size(); ++i) {
            int h = heights[i];
            int w = right[i] - left[i] - 1;

            int area = h * w;
            max_area = max(area, max_area);
        }

        return max_area;
    }
};
