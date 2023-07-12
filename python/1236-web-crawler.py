# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        '''
        BFS graph problem (Queue)

        Time: O(n + e) where n is the number of nodes and e is the number of edges
        Space: O(n)
        '''

        split_url = startUrl.split('/')
        hostname = split_url[0] + '//' + split_url[2]

        q = collections.deque([startUrl])
        visited = set([startUrl])

        while q:
            url = q.pop()
            neighboring_urls = htmlParser.getUrls(url)
            for neigh in neighboring_urls:
                if neigh.startswith(hostname) and neigh not in visited:
                    q.append(neigh)
                    visited.add(neigh)
        return list(visited)
