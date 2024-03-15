/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
    // Time: O(n)
    // Space: O(1)
    //  leetcode doesnt count the extra space used for the
    //  results which is why it is not O(n)

    let dp = [];
    running_product = 1;
    for (let i = 0; i < nums.length; i += 1) {
        running_product *= nums[i];
        dp.push(running_product);
    }

    running_product = 1;
    for (let i = nums.length - 1; i >= 0; i -= 1) {
        const pre = i > 0 ? dp[i - 1] : 1;
        dp[i] = pre * running_product;
        running_product *= nums[i];
    }

    return dp;
};
