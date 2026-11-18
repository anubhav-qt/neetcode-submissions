class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        vector<int> left(n, -1), right(n, n);
        stack<int> left_expansion, right_expansion;

        for (int i = 0, j = n - 1; i < n; ++i, --j) {
            while (!left_expansion.empty() && heights[left_expansion.top()] >= heights[i]) {
                left_expansion.pop();
            } if (!left_expansion.empty()) {
                left[i] = left_expansion.top();
            } left_expansion.push(i);

            while (!right_expansion.empty() && heights[right_expansion.top()] >= heights[j]){
                right_expansion.pop();
            } if (!right_expansion.empty()) {
                right[j] = right_expansion.top();
            } right_expansion.push(j);
        }
        
        int max_area{0};
        for (int i = 0; i < n; ++i) {
            int height = heights[i];
            int width = right[i] - left[i] - 1;
            int area = height * width;

            max_area = max(area, max_area);
        }

        return max_area;
    }
};
