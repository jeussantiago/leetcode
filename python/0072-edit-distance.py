class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        - if characters at the same index are the same, then we can remove it since we don't do anything to it

        word 1: abd
        word 2: acd
        - first pos is the same character so leave it alone, move both pointers over
        (i+1, j+1 or word1=word1[i+1:], word2=word2[j+1:]) -- (bd, cd)
        - second position:
            - inserting: insert the c in front of the b (acbd), this takes care of the matching characters => move the second word pointer over
            (j+1 or word2=word2[j+1:]) -- (cbd, cd)
            - delete: delete word 1 character (ad) => ignore that character now, move the first word pointer over
            (i+1 or word1=word1[i+1:]) -- (d, cd)
            - replace: replace word 1 character with word 2 character => since both characters are the same, move both pointer over by one
            (i+1, j+1 or word1=word1[i+1:], word2=word2[j+1:]) -- (cd, cd)
        
        Dynamic Programming:
        - store the minimum amount of operations at dp positions
        X: current pos
        I: insert (j+1)
        D: delete (i+1)
        R: replace (i+1, j+1)

                    word2
                   a  c  d  | base case(length of the empty strings) 
                  ---------------------  
                a|          | 3 len(abd)
        word1   b|    X  I  | 2 len(bd)
                d|    D  R  | 1 len(d)
                  ---------------------  
        base case| 3  2  1  | 0

        - pos 1 (a matches) => i+1, j+1
        - pos 2 (b and d doesn't match), figure out the min operations between inserting, deleting, and replacing
        (x is current pic in diagram, I, D, R show where pointer would be if you insert, delete, or replace)

        ---------------------------------------------------------------------------------
        - Since we have base cases , we can check which one of the current position's neighboring box has the minimum number
        - we can come to this conclusion because we check the locations where you would end up if you: 
        insert (j+1), right of current box
        delete (i+1), under of current box
        replace (j+1, i+1), down and right of current box
        - the base cases tells us how many operations would need if the opposite word was an empty string
        (Ex: word1:bd, word2:"", 2 delete operations)
        (Ex: word1:"", word1:"d", 1 insert operation)
        - So we work bottom up and compute from the pos(-1,-1) 
                            word2
                   a  c  d  | base case
                  ---------------------  
                a| 1  2  2  | 3 len(abd)
        word1   b| 2  1  1  | 2 len(bd)
                d| 2  1  0  | 1 len(d)
                  ---------------------  
        base case| 3  2  1  | 0

        ** if the characters are equal, ignore character by taking the value of i+1 and j+1
        ** if the characters are not equal, take the minimum number and +1

        Time: O(m * n) where m is the length of word1 and n is the length of word2
        Space: O(m * n) where m is the length of word1 and n is the length of word2
        '''
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]

        #fill dp with base case
        for i in range(len(word1)):
            dp[i][len(word2)] = len(word1) - i

        for j in range(len(word2)):
            dp[len(word1)][j] = len(word2) - j

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    # equal characters - ignore character by taking value from diagonal
                    dp[i][j] = dp[i+1][j+1]
                else:
                    # non equal characters - take minimum and add 1 for a single operation
                    insert = dp[i][j+1] #right
                    delete = dp[i+1][j] #down
                    replace = dp[i+1][j+1] #diagonal, down and right
                    #add 1 for the operation of inserting, deleting or replacing
                    dp[i][j] = 1 + min(insert, delete, replace)

        return dp[0][0]




        '''
        Recursive Solution:

        **Doesn't work because of timelimit
        '''

        # if not word1 and not word2:
        #     return 0
        # if not word1:
        #     # to turn word1 into word2: insert characters into word1 until reach word2
        #     return len(word2)
        # if not word2:
        #     # to turn word1 into word2: delete characters into word1 until reach word2
        #     return len(word1)
        # if word1[0] == word2[0]:
        #      # matching characters, ignore and go to next character
        #     return self.minDistance(word1[1:], word2[1:])
        # insert = 1 + self.minDistance(word1, word2[1:])
        # delete = 1 + self.minDistance(word1[1:], word2)
        # replace = 1 + self.minDistance(word1[1:], word2[1:])
        # return min(insert, replace, delete)
