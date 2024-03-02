/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
    /**
     * Time: O(n)
     * Space: O(1)
     */

    let ptr = 1;
    for (let i = 1; i < nums.length; i += 1) {
        if (nums[i] !== nums[i - 1]) {
            nums[ptr] = nums[i];
            ptr += 1;
        }
    }

    return ptr;
};
