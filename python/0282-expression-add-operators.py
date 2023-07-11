class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        '''
        2 + 3 * 2
        dealing with multipication
        curr_num = 2
        prev_num = 3
        curr_total = 5

        - to multiple, subtract the prev_num from  the curr_total
        5 - 3 = 2
        - add what would be the multiplication
        2 + (3 * 2) = 2 + 6 = 8
        - the prev_num is now the multiplicaton -> (3 * 2)

        - for + and -, we pass in the opposit previous number clearly because we need to 
        do reverse operation

        Time: O(4^n) 4 decision each time, the height of the tree is lenght of num (n)
        Space: O(4^n)

        https://www.youtube.com/watch?v=8wmks4LX2F8&ab_channel=TimothyHChang
        '''
        res = []
        N = len(num)

        def dfs(i, exp, total, prev_num):
            if i >= N:
                if total == target:
                    res.append("".join(exp))
                return

            for j in range(i, N):
                val = int(num[i:j+1])
                if not exp:
                    dfs(j+1, [num[i:j+1]], val, val)
                else:
                    dfs(j+1, exp + ["+"] + [num[i:j+1]], total + val, val)
                    dfs(j+1, exp + ["-"] + [num[i:j+1]], total - val, -val)
                    dfs(j+1, exp + ["*"] + [num[i:j+1]], (total -
                        prev_num) + (prev_num * val), (prev_num * val))

                # to avoid repeating 0, stop after the first loop
                if val == 0:
                    break

        dfs(0, [], 0, None)
        return res
