class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        int max_count{0};
        for (int num: nums) {
            ++count[num];
            max_count = max(max_count, count[num]);
        }

        vector<vector<int>> frequency_bucket(max_count + 1);
        for (const auto& pair: count) frequency_bucket[pair.second].push_back(pair.first);

        vector<int> res;
        res.reserve(k);
        for (int i = max_count; i >= 1; --i) {
            for (int num: frequency_bucket[i]) {
                res.push_back(num);
                if (res.size() == k) return res;
            }
        }

        return res;
    }
};
