/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function (s, t) {
    // Time: O(n)
    // Space: O(1)
    //      ; max items in hash map is 26

    const iso = new Map();
    const used = new Set();
    for (let i = 0; i < s.length; i++) {
        if (s[i] in iso) {
            if (iso[s[i]] !== t[i]) {
                return false;
            }
        } else {
            if (used.has(t[i])) {
                return false;
            }
            iso[s[i]] = t[i];
            used.add(t[i]);
        }
    }

    return true;
};
