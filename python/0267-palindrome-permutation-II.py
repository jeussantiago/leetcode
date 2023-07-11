class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        '''
        s = aabb
        {
            a: 2
            b: 2
            c: 1
        }



        - figure out if a palindrome is possible
            - return false if a palindrome is not possible
            - return true if a palidnrome is possible
                - if even, accompany with tuple a -1
                - if odd, accompany with tuple the character which is odd


        - if theres an odd number, definitely have to put that one in first
        - if theres an even number then it doesn't matter


        Time: O(n^ logn)
        Space: O(n)
        '''
        counter = collections.Counter(s)

        # returns false if not palindrome
        # returns true if palindrom, along with index if it in odd
        def isPalindromePossible(counter):
            odd_char = None
            odd_count = 0
            for c, val in counter.items():
                if val % 2:
                    odd_count += 1
                    if odd_count > 1:
                        return (False, -1)
                    odd_char = c

            return (True, odd_char)

        def createPalindromePermutation(counter, strng, num_remaining_letters):
            res = []

            if num_remaining_letters == 0:
                return [strng]

            for c in counter:
                if counter[c] > 0:
                    counter[c] -= 2
                    permutation = createPalindromePermutation(
                        counter, c + strng + c, num_remaining_letters - 2)
                    res.extend(permutation)
                    counter[c] += 2

            return res

        isPalindrome, odd_char = isPalindromePossible(counter)

        # unable to create palindrome from given letters
        if not isPalindrome:
            return []
        # create palindrome strings
        num_remaining_letters = sum(counter.values())
        if odd_char:
            counter[odd_char] -= 1
            num_remaining_letters -= 1
            res = createPalindromePermutation(
                counter, odd_char, num_remaining_letters)
        else:
            res = createPalindromePermutation(
                counter, "", num_remaining_letters)

        return res
