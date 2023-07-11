class Twitter:

    def __init__(self):
        self.time = 0
        self.follow_map = collections.defaultdict(set)
        self.tweet_map = collections.defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.time, tweetId))
        self.time -= 1

    '''
    k is the user follow list length ; n is the number of tweets by a person
    Time: O(k) ; (k) to add k user's tweets to all the tweets
                (k) heapify - faster than (klogk) to each each tweet to the heap individually
    Space: O(k * n)
    '''

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []

        # create a list of the tweets of the user and user that it follows
        follow_lst = list(self.follow_map[userId]) + [userId]

        for user in follow_lst:
            if user in self.tweet_map:
                minHeap.extend(self.tweet_map[user])

        # sort by adding to a heap based on the time - python only has minHeap so thats why time is negative
        heapq.heapify(minHeap)

        # get the last 10 tweets
        newsFeed = []
        while minHeap and len(newsFeed) < 10:
            newsFeed.append(heapq.heappop(minHeap)[1])

        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
