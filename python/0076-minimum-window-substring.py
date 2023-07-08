class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        find the shortest word in s with all the characters in t
        (hash table and sliding window)

        ADOBECODEBANC
        |    | (current shortest character with all characters in t - all values in hash table are 0)
        have: 3 ; count: 3
        since have == count: update min window

        ADOBECODEBANC
        |    |   | 
        (third line represents a repeating character showing up; count in hash table for B goes from 1 to 2 )
        (have 3: need: 3 doesn't change b/c we have all the characters in T present)
        - move left window over
        ADOBECODEBANC
         |   |   | 
        (remove A, puts the counter of A to less than the needed amount so that means the string is not valid anymore )
        (have 2: need: 3)
        - move right window until the numbers in hash table match again

        ADOBECODEBANC
         |   |   || 
        (have 3: need: 3)
        - if have == need
            - min(current string, result)
            - left pointer += 1
        
        Solution:

        if character in t:
            - increase the countWindow[current character] += 1
            if countWindow[current character] <= countT[current character]
                - increase have += 1
        
        #remove all characters on the left that aren't in T
        while have == need
            if result == ""
                result = window
            else
                min(window, result)

            if character at left pointer in T:
                - decrease countWindow[left pointer character] -= 1
                if countWindow[left pointer character] < countT[left pointer character]
                    - decrease have -= 1
            left pointer += 1

        - increase right side of window += 1
        

        Time: O(n) where n is the size of the s string : pass through the s string one time - sliding window
        Space: O(T + T) where T is the number of characters in string t kept in a hash table (2 hash tables for window and count T)
             : O(T)
        '''
        result, resultLen = "", float('infinity')
        countT = collections.Counter(t)
        countWindow = dict.fromkeys(t, 0)
        have, need = 0, len(t)
        leftPointer, rightPointer = 0, 0

        while rightPointer < len(s):
            c = s[rightPointer]
            if c in t:
                countWindow[c] += 1
                if countWindow[c] <= countT[c]:
                    have += 1
            
            while have == need:
                currentLen = rightPointer - leftPointer + 1
                if currentLen < resultLen:
                    resultLen = currentLen
                    result = s[leftPointer: rightPointer+1]

                left_c = s[leftPointer]
                if left_c in t:
                    countWindow[left_c] -= 1
                    if countWindow[left_c] < countT[left_c]:
                        have -= 1

                leftPointer += 1

            rightPointer += 1
        
        return result






























