class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        '''
        DFS:

        n is the number of words in list. m is the length of a word
        Time: O(n^2 * m) ; O(n^2) creating the adjacency list - can't really get around comparing every single word to each other
                         ; O(m) dfs through the adjacency list

        Space: O(n^2) ; the adjacency list will have at most n^2 combination of edges
        '''
        def isSimilar(word1, word2):
            # base case that there are repeating words in strs
            if word1 == word2:
                return True

            # a word is similar to another word if you can swap 2 chars and they are the same word or
            # if the amount of incorrect char positions is exactly 2
            incorrect_char_pos_cnt = 0
            for i in range(len(word1)):
                if incorrect_char_pos_cnt > 2:
                    break

                if word1[i] != word2[i]:
                    incorrect_char_pos_cnt += 1

            return incorrect_char_pos_cnt == 2

        # find out which words are similar to each other
        # create an adjancency list from those word
        adj = collections.defaultdict(list)
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if isSimilar(strs[i], strs[j]):
                    # bidirectional to make traversing easier
                    adj[i].append(j)
                    adj[j].append(i)

        # traverse the adjacency list to find out how many groups there are
        visited = set()

        def dfs(idx):
            visited.add(idx)
            for neigh in adj[idx]:
                if neigh not in visited:
                    dfs(neigh)

        groups = 0
        for i in range(len(strs)):
            if i not in visited:
                dfs(i)
                groups += 1

        return groups
