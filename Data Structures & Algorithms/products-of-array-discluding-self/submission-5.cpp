// a simple algorithm to return a new array, each of its index containing the product of all nums except that index in the input
// algorithm:
// initialize vector<long long> output and prefix_product and postfix_product, all length = nums.size() and filled with 1s
// for each index (from second onwards) in nums: prefix_product[index] = prefix_product[index - 1] * nums[index]
// for each index (from secondlast onwards) in nums: postfix_product[index] = postfix_product[index + 1] * nums[index]
// for each index in output: output[index] = prefix_product[index] * postfix_product[index]
// return output

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int length = nums.size();
        vector<int> output(length, 1), prefix_product(length, 1), postfix_product(length, 1);

        for (int i = 1, j = length - 2; i < length; ++i, --j) {
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1];
            postfix_product[j] = postfix_product[j + 1] * nums[j + 1];
        }

        for (int i = 0; i < length; ++i) {
            output[i] = prefix_product[i] * postfix_product[i];
        }

        return output;
    }
};
