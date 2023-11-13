class Solution:
    def sortVowels(self, s: str) -> str:
        '''
        - take advantage of the fact that there are only 5 lower case
        vowels and corresponding vowels
            - in this way, we know how much space it will use

        - track how many times a vowel appears (upper and lower)
        - go through the string another time
        - if the character is a consonant, add to the results
        - if the character is a vowel
            - iterate through this ordered vowels "AEIOUaeiou"
            (its already sorted in ASCII increasing value)
            - if the current character is not 0 in the frequency map,
            then add the vowel to the results
            - if the character is 0, then go to the next character that
            doesn't have 0

        Time: O(n)
            ; (n) iterating through the string twice
        Space: O(1)
            ; (1) we use space for the frequency map but we know the 
            ; size of it to be 10 (5 for lower case vowels and 5 for
            ; upper case)
        '''
        sortedVowel = "AEIOUaeiou"
        freq = collections.defaultdict(int)
        for c in s:
            if c in sortedVowel:
                freq[c] += 1

        res = ""
        vowel_ptr = 0
        for c in s:
            if c not in sortedVowel:
                res += c
            else:
                while freq[sortedVowel[vowel_ptr]] == 0:
                    vowel_ptr += 1

                freq[sortedVowel[vowel_ptr]] -= 1
                res += sortedVowel[vowel_ptr]

        return res

    def sortVowels(self, s: str) -> str:
        '''
        - consonants stay in the same place
        - vowels get sorted

        - we don't know what vowel is going to appear, so we need to scan
        the entire string first to know what we're working with before we
        can sort them

        sorting of vowels:
            - get the ASCII value of the vowel and insert
            it into a minHeap (ASCII_value, original_vowel)

        creating the new string:
            - loop through original string
            - if consonant
                - add to new_string
            - if vowel:
                - pop from minHeap
                - add onto new_string

        Time: O(nlogn)
            ; (n) initial scan
            ; (logn) adding to heap
            ; (n) scanning the string a second time
            ; (logn) popping from the heap
            ; (nlogn + nlogn) => (nlogn)
        Space: O(n)
            ; (n) minHeap - worst case: the entire string gets added to
            ; the heap (string is all vowels)
        '''
        vowels = 'aeiou'
        minHeap = []
        for c in s:
            if c.lower() in vowels:
                heappush(minHeap, (ord(c), c))

        res = ""
        for c in s:
            if c.lower() in vowels:
                res += heappop(minHeap)[1]
            else:
                # consonant
                res += c

        return res
