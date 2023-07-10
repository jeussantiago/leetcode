class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        hot - *ot       dot - *ot
            - h*t           - d*t
            - ho*           - do*

        adjacency list:
        {
            *ot : [hot, dot, lot]
            h*t : [hot, hit]
            ho* : [hot]
            d*t : [dot]
            do* : [dot]
        }

        - go through every word which is (n) and go through every character which is (m)
        - add each word to the list is (m)
        - O(n * m^2)

        hit - hot - dot - dog ---|
                |    |     |     | 
                --- lot - log    |  
                           |     |
                          cog ---|

        - go along each edge once, never twice
        - go through each word (n^2) and find each neighbor (m)
        - O(n^2 * m)

        - even though theres an edge between "dot" and "lot", we don't want to visit that because 
        it is visiting the same node twice


        Time: O()
        Space: O()
        '''

        if endWord not in wordList:
            return 0

        # create an empty list when you create a new key
        neighbor = collections.defaultdict(list)
        wordList.append(beginWord)
        # create adjacency list
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbor[pattern].append(word)

        # bfs
        # search through the adjacency list to find the quickest way to the endWord
        visitedWord = set([beginWord])
        queue = deque([beginWord])
        res = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res

                # check the new pattern
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighborWord in neighbor[pattern]:
                        if neighborWord not in visitedWord:
                            visitedWord.add(neighborWord)
                            queue.append(neighborWord)
            res += 1

        return 0
