class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        '''
        bulls = right number , right place
        cows = right number , wrong place

        - counter for secret
        secret = "1123"
        {
            1: 2
            2: 1
            3: 1
        }

        - run through both of them again
        - if secret[i] == guess[i]
            - bull += 1
        elif guess[i] in secret_counter
            - check if the counter > 0
                - if it is, increase cows += 1
                - reduce counter in counter


        - its fine if the secret number is longer than the guess number
        secret = "1123" ; guess = "24"
        - not fine if the secret is shorter than the guess
        secret = "24" ; guess = "1123"
            - we need to check every number in guess with corresponding character in secret
            - probably just give secret[i] a none value

        Time: O(n + m) run through secret string (n) ; then run through length of guess (m)
        Space: O(n) for secret_counter
        '''

        secret_count = collections.Counter(secret)

        bulls = 0
        cows = 0
        for i, guess_c in enumerate(guess):
            if guess_c in secret_count:
                secret_c = None if i >= len(secret) else secret[i]
                if guess_c == secret_c:
                    bulls += 1
                    # if there is no extra count for the num to compensate for thinking it
                    # was a cow earlier, then reduce the number of cows
                    # turning the cows into bulls
                    if secret_count[guess_c] <= 0:
                        cows -= 1
                else:
                    if secret_count[guess_c] > 0:
                        cows += 1
                secret_count[guess_c] -= 1

        return f'{bulls}A{cows}B'
