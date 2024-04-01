/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
    // Time: O(n)
    // Space: O(1)

    const split_s = s.split(" ");
    let last_word_len = 0;
    for (let i = 0; i < split_s.length; i++) {
        if (split_s[i].length > 0) {
            last_word_len = split_s[i].length;
        }
    }

    return last_word_len;
};
