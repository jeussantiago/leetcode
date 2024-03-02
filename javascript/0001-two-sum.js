/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    /**
     * Time: O(nlogn)
     * Space: O(n)
     */
    const N = nums.length;
    var new_nums = [];
    for (let i = 0; i < N; i += 1) {
        new_nums.push([nums[i], i]);
    }

    nums = new_nums.sort((a, b) => a[0] - b[0]);
    let left = 0;
    let right = N - 1;

    while (left < right) {
        let total = nums[left][0] + nums[right][0];
        if (total === target) {
            return [nums[left][1], nums[right][1]];
        }

        if (total < target) {
            left += 1;
        } else {
            right -= 1;
        }
    }
};

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    /**
     * Hash Map - One pass
     *
     * Time: O(n)
     * Space: O(n)
     */

    let seen = new Map();
    for (let i = 0; i < nums.length; i += 1) {
        let remain = target - nums[i];
        if (remain in seen) {
            return [seen[remain], i];
        }

        seen[nums[i]] = i;
    }
};
