class Solution {
public:
    int trap(vector<int>& height) {
        int length = height.size();
        vector<int> left_max(length), right_max(length);

        // fill the left_max vector
        for (int i = 1; i < length; ++i)
            left_max[i] = max(left_max[i - 1], height[i - 1]);

        // fill the right_max vector
        for (int i = length - 2; i >= 0; --i)
            right_max[i] = max(right_max[i + 1], height[i + 1]);

        int res{0};
        for (int i = 0; i < length; ++i)
            res += max((min(left_max[i], right_max[i]) - height[i]), 0);
        
        return res;
    }
};
