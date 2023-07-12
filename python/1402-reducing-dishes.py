class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        '''
        Greedy (Prefix Sum):
        - sort

        [1,0,0,0,20]
        - we want all the dishes with the highest satisfactions at the end,
        these will get the biggest multiplications
        - but we don't necessarily know when it'll appear after the dishes, but we do know it'll come
        Idea:
        - if we add the last satisfaction rating as many times as possible until the satisfaction is negative,
        then it would be the same thing as multiplying it by some n value
        - in the case above:
            20 + 20 + 20 + 20 + 20 == (20 * 5)
        so, at each position, going in reverse, we can just add the previous satisfication ratings
        - to make sure we don't do repeated work, we can use the prefix sum algorithm and just add the satisfaction totals
        - if the prefixSum goes into the negative, then theres no reason to continue since the sum will just get smaller and smaller

        Time: O(nlogn) sorting
        Space: O(logn) no extra space is used but languages use extra space when sorting, such as quicksort
        '''
        satisfaction.sort()
        prefixSum = 0
        res = 0
        for i in range(len(satisfaction)-1, -1, -1):
            rating = satisfaction[i]
            prefixSum += rating
            if prefixSum < 0:
                break

            res += prefixSum

        return res
