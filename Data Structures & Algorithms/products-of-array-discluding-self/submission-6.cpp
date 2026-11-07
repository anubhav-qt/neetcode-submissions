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
        vector<int> output(length, 1);
        int prefix {1}, postfix {1};

        for (int i = 0, j = length - 1; i < length; ++i, --j) {
            output[i] *= prefix;
            prefix *= nums[i];

            output[j] *= postfix;
            postfix *= nums[j];
        }

        return output;
    }
};
