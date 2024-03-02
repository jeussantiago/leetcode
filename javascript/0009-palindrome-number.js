/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
    x = x.toString();
    let reverseWord = "";
    for (let i = 0; i < x.length; i += 1) {
        reverseWord = x[i] + reverseWord;
    }

    return x === reverseWord;
};
