// algorithm to return an array of k most frequent elements from nums
// algorithm:
// initialize hash map (freq) of keys and values as num and its count in nums
// fill freq -- O(n)
// initialize a vector<vector<int>> (freq_bucket) with size = nums.size() + 1
// for each key, value pair in freq, push_back(key) in freq_bucket[value]
// start from the end and keep filling the output array till the first k elements from the end

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (const int& num : nums) {
            ++freq[num];
        }

        vector<vector<int>> freq_bucket(nums.size() + 1);
        for (auto& [key, value] : freq) {
            freq_bucket[value].push_back(key);
        }

        vector<int> output;
        for (int i = (int)freq_bucket.size() - 1; i >= 0 && k > 0; --i) {
            if (freq_bucket[i].size() > 0) {
                for (const int& num : freq_bucket[i]) {
                    output.push_back(num);
                    if (--k <= 0) break;
                }
            }
        }

        return output;
    }
};
