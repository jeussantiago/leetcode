class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        '''
        Time: O(n * goal)
        Space: O(n * goal)
        '''
        MOD = 10**9 + 7
        cache = {}

        def countPlaylist(goal, old_songs):
            # reached the goal and went through all the possibel list of songs (n)
            if goal == 0 and old_songs == n:
                return 1

            # the number of old songs should never exceed the possible list of songs (n)
            if goal == 0 or old_songs > n:
                return 0

            # already done this combination of goal(number of songs left to add) and old_songs(number of songs available)
            if (goal, old_songs) in cache:
                return cache[(goal, old_songs)]

            # choose a new song
            # recur number of songs in playlist increased so decrement goal,
            # when a new song is used, can add song to list of old songs by increamenting count of old_songs
            # multipy by number of available new songs left
            res = countPlaylist(goal - 1, old_songs + 1) * (n - old_songs)

            # choose an old song
            if old_songs > k:
                # number of songs in playlist increased so decrement goal
                # since we chose an old song, we leave the count of it alone since we're not adding a new unique song back into the mix
                # multiply by the number of old songs available that is greater than k
                res += countPlaylist(goal - 1, old_songs) * (old_songs - k)

            cache[(goal, old_songs)] = res % MOD
            return cache[(goal, old_songs)]

        return countPlaylist(goal, 0)
