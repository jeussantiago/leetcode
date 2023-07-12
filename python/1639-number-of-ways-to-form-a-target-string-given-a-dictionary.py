class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        '''
        - can only choose 1 char per index in the words list
        ** DP is faster than hashmap since you don't have to take time to hash items but converting one to another is too difficult and
        don't think people care too much if you use either or

        ["acca","caca", "aabb"] ; "aca"

        Create a count of each letter in each index:

        {
            (0, a): 2
            (0, c): 1
            (1, a): 2
            (1, c): 1
            (2, c): 2
            (2, b): 1
            (3, a): 2
            (3, b): 1
        }

        DFS:

        - if target_ind > len(target): return 1 
        (successful combination found)

        - if word_ind > len(word[0]): return 0
        (no more combination found)

        - check the cache

        - call dfs
            - situation of skipping the current index
            (increase word_ind ; keep target_ind same)
            - situation of taking the count of the current index
            (take count from counter ; multiply(*) ; dfs where you advance positions)


        Cache:

        - (curr_word_ind, target_ind) : count of how many combinations to create target at that given word index and target index

        {
            (2, 2) : 4
        }

        - there are 4 ways to create the target word at this position
        - ind 0 will skip itself and ind 1 will take that (2,2) and multiply that by its count of "a"
            - index 1 will have 2 * 4 = 8

        - theres also the situation where 0 won't skip but will skip ind 1 and thus we need the cache data because it matches
        with (2,2)
            - it would return 4 when we hit (2,2)

            - it will add that cached data to the situation of not skipping 1

        - if the character doesn't exist inn that word_ind
            - it will multiply the total by 0
            - this will prevent combinations that shouldn't exist

        W is the lengt of words list ; K is the len of a word ; T is the length of the target word
        Time: O(W * K + T * K) 
                  ; O(W * K) to create count dictionary
                  ; O(T * K) to do dfs
            : O(T * K)
        Space: O(26 * K + T * K)
                  ; O(26 * K) for count dict
                  ; O(T *K) for cache
             : O(T * K)
        '''
        mod = 10**9 + 7

        cnt = collections.defaultdict(int)
        for word in words:
            for i, c in enumerate(word):
                cnt[(i, c)] += 1

        cache = {}

        def dfs(word_ind, target_ind):
            if target_ind == len(target):
                return 1

            if word_ind == len(words[0]):
                return 0

            if (word_ind, target_ind) in cache:
                return cache[(word_ind, target_ind)]

            # skip current index
            cache[(word_ind, target_ind)] = dfs(word_ind + 1, target_ind)

            # take the count of current index
            char_cnt_at_ind = cnt[(word_ind, target[target_ind])]
            cache[(word_ind, target_ind)] += char_cnt_at_ind * \
                dfs(word_ind + 1, target_ind + 1)

            return cache[(word_ind, target_ind)] % mod

        return dfs(0, 0)
