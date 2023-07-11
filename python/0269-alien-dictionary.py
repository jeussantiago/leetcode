class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        ["wrt","wrf","er","ett","rftt"]

        - index positions tells which comes before the other since the words are lexicogrtaphically sorted already

        "ett" and "rftt"
        - e comes before r
        - t comes before f
        - t is the same character as t

        word1 = "ett" ; word2 = "rftt"
        (** can only do this until the minimum length of the two words)

        index = 0
        - word1[0] (e) comes before the same index in word2
            (add the next char to the list)
            adj_list[word1[0]] .append(word2[0])

        - if the characters are the same, then don't do anything

        - if we find two characters that are different
            - add to set then
            - break
            (we break b/c we only care about the first wrong char comparisons)

        {
            w: e
            r: t
            t: f
            f: 
            e: r
        }

        Invalid list of words:
        - invalid means that there is a cycle

        [we, ee, we]
        - w comes before e
        - but then we see that e comes before w
        - this means that there is a loop and the wors list is invalid

        Base Case (Invalid):
        - if the prefix of the 2 comparing words is the same, the shorter word should be lexicographically order or
        comes before the longer word
        - so if you see that they have the same prefix, it is fine if the first word is shorter
            word1 = wrf ; word2 = wrfs <====== Valid
        - not fine if the first word is longer
            word1 = wrfs ; word2 = wrf <====== Not Valid



        SEARCHING THROUGH ADJACENCY LIST (dfs)
        - work from the bottom up
        - if the character has a neighbor, go to that neighbor
        - if the character doesn't have a neighbor, 
            add the character to the output/return the char

        - add each letter to a visited set to avoid adding repeated letters after have gone through all its children

        - To avoid cycles, we can add the letter to another set
        - will do this just before entering a neighbor

        - can also use a dictionary
        - adding something to the dictionary will show that its in a visited set
        - the value will be True or False to tackle the cycle issue

        - DFS returns [f, t, r, e w]
        - reverse

        Time: O(n) where n is the number of unique characters in the word list
        Space: O(n)
        '''
        # create adjacency list
        adj_lst = {}
        for word in words:
            for c in word:
                adj_lst[c] = set()

        # fill adjacency list
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            # base case where words are not sorted lexicogeraphically
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj_lst[w1[j]].add(w2[j])
                    break

        # traverse adjacency list

        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                # if True, char is a cycle
                # if False, char already in results
                return visited[char]

            visited[char] = True
            # go through neighbors
            for neighbor in adj_lst[char]:
                if dfs(neighbor):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj_lst:
            if dfs(char):
                # cycle
                return ""

        return "".join(res[::-1])
