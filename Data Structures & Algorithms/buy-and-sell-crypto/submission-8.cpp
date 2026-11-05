class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l{0}, r{0}, profit{0}, max_profit{0};
        while (r < prices.size()) {
            if (prices[r] > prices[l]) {
                profit = prices[r] - prices[l];
                max_profit = max(max_profit, profit);
            } else {
                l = r;
            }
            ++r;
        }

        return max_profit;
    }
};
