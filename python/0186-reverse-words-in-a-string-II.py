class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        - reverse every position
        (every word is now on the other side of the array, but every word is reversed)
        ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
        [e, u, l, b, "", s, i, "", y, k, s, "", e, h, t]
        (words are correct order, just reversed)

        - reverse each word
            - 2 pointers -> one at the start of the word, one at the end of the word
            - if next index is the length of the aray OR
            if next char is a " "

            - while loop to reverse until left > right 

        Time: O(n)
        Space: O(1)
        """
        N = len(s)
        # reverse the array
        left, right = 0, N - 1
        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        # reverse each word
        left = 0
        for i in range(N):
            if i == N-1 or s[i + 1] == " ":
                right = i
                while left < right:
                    s[left], s[right] = s[right], s[left]

                    left += 1
                    right -= 1

                # advance left pointer to next word
                left = i + 2
