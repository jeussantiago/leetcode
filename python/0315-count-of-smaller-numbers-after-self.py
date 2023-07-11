from sortedcontainers import SortedList
# from bisect import bisect_left


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        '''
        - we can work backwards and keep an order list of  the nums we encounter
        nums = [5,2,6,1]
        [1] -> [1,6] -> [1,2,6] -> [1,2,5,6]

        - we need to know where we insert the number into the list
            - using binary search/bisect_left we can find the insert position in O(logn)


        - inserting into a list is O(n)
        - to optimize this, we are going to use sortedcontainers.SortedList
            - this has a time complexity of O(logn) to insert
            - it uses a heap in the background to keep the order


        - go through the nums in reverse
            - find where to insert the current number in the sorted list (bisect_left)
                - the insert position also tells us how many smaller numbers are after thecurrent number
                - since we traverse backwards, we see the later numbers first
                - this means that if you put a number into the sorted list, all the numbers currently
                present appear after the current number
                - the index to insert the current number is also how many numbers are less than itself
                Ex: [1,6]
                    - insert 2 at index 1
                    - this would become [1,2,6]
                    - this means that there is 1 number less than 2
                - record the index as the result
            - insert into sorted_list

        - there might be duplicates in the nums [5,2,2,2,6,1]
        - we use bisect_left rather than bisect_right because anything we add to the list appears later, but we don't want 
        to include the other duplicates since duplicates are not less than the value
            - we only want to include the value < itself

        TIme: O(n * (logn + logn)) where n is the len of nums ; go through each number -> at each number, find where to insert
            using binary search/bisect_left -> then insert using sortedcontainers which uses heaps in the background to add
            : O(nlogn)
        Space: O(n)
        '''

        sorted_lst = SortedList()
        res = []
        for n in nums[::-1]:
            ind = sorted_lst.bisect_left(n)
            sorted_lst.add(n)
            res.append(ind)
        return res[::-1]
