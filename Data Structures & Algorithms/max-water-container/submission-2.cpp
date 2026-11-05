class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l{0}, r = heights.size() - 1, max_area{0}, area{0};
        while (l < r) {
            area = (min(heights[l], heights[r])) * (r - l);
            max_area = max(area, max_area);
            if (heights[l] <= heights[r]) ++l;
            else --r;
        }

        return max_area;
    }
};
