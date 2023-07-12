class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        '''
        - valid transfer is if there is a cycle in the loop
        - find the biggest cycles/loops that don't collide

        - if there is a valid transfer/loop
            - need to keep track of the people that were successfully transferred
            - if there are multiple cycles, then just take the ycycle with the biggest count

        cycle = [0,1]

        n is the number of buildings
        m is the number of requests
        Time: O(2^m * n)
            ; (2^m) loop over every possible requests twice
            ;   2 decisions each time and the height of tree is number of requests
            ; (n) at the end, when we reach the leaf nodes/the end of the reqeusts, we have to check over each building to 
            ; see if they are all 0/no vacnt spots
        Space: O(m + n)
            ; (m) recursion stack
            ; (n) vacancy array
        '''
        self.res = 0
        # negative means vacant spot in vuilding, positive means overcrowded in building
        vacancy = [0] * n

        def backtrack(curr_request_ind, num_request_accepted):

            if curr_request_ind == len(requests):
                # after going through all the request
                # check to see if all the vacancy spots have been filled
                # (if a number other than 0 exist, then an unsuccessful transfer is present)
                if all(spot == 0 for spot in vacancy):
                    self.res = max(self.res, num_request_accepted)
                return

            # don't take the request
            backtrack(curr_request_ind + 1, num_request_accepted)

            # take the transfer request
            building_from, building_to = requests[curr_request_ind]
            # create vacancy slot for the building leaving and building to is overcrowded with an extra person
            vacancy[building_from] -= 1
            vacancy[building_to] += 1
            backtrack(curr_request_ind + 1, num_request_accepted + 1)
            vacancy[building_from] += 1
            vacancy[building_to] -= 1

        backtrack(0, 0)
        return self.res
