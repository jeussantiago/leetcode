class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        '''
        n is the length of transactions
        Time: O((n−1)!)
            ; brute force, at every position, have to explore n-1 positions
        Space: O(n)
            ; debt map and debt list 
        '''
        # dict to show how much people are owed or are in debt
        # - positive means that they are owed money
        # - negative means that they are in debt
        debt_map = collections.defaultdict(int)
        for person_a, person_b, amount in transactions:
            debt_map[person_a] += amount
            debt_map[person_b] -= amount

        # we don't care about the people who have net 0 total debt
        debt = [amount for amount in debt_map.values() if amount != 0]
        N = len(debt)

        def dfs(idx):
            # earlier debts might have been settled (net debt == 0), skip those people
            while idx < N and debt[idx] == 0:
                idx += 1

            if idx == N:
                return 0

            num_transactions = float('inf')
            for j in range(idx + 1, N):
                # if you have someone with debt, you want to pair them up with someone who is owed money
                # viceversa, if you have someone that is owed money, you want to pair them up with someone who has debt
                # this kills 2 issues at once
                # also want to skip the people with settled debts (net debt == 0)
                if debt[j] * debt[idx] < 0:
                    # settle up the debt
                    debt[j] += debt[idx]
                    # go to the next index
                    num_transactions = min(num_transactions, 1 + dfs(idx + 1))
                    # make a scenario where the debt wasn't settled - set debt back to original amount
                    debt[j] -= debt[idx]

            return num_transactions

        return dfs(0)
