class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        '''
        - figure out what the first 2 numbers are

        T: O(n^2)
        S: O(1)
        '''

        def validNum(n):
            if len(n) == 1:
                # [0,1,2,3,4...]
                return True

            if n[0] == "0":
                # [01,02,04] - not valid
                return False
            return True

        def isAdditive(first_num, sec_num):
            i = len(first_num) + len(sec_num)
            while i < len(num):
                n_added = str(int(first_num) + int(sec_num))
                third_num = num[i: i + len(n_added)]
                if n_added != third_num:
                    return False

                first_num, sec_num = sec_num, third_num
                i += len(n_added)
            return True

        N = len(num)

        def find_first_sec_num():
            for i in range(1, math.ceil(N/2)):
                n1 = num[:i]
                if not validNum(n1):
                    continue
                for j in range(i+1, N - (N//4)):
                    n2 = num[i:j]
                    if not validNum(n2):
                        break

                    n_added = str(int(n1) + int(n2))
                    n3 = num[j: j + len(n_added)]

                    if n_added == n3:
                        if isAdditive(n1, n2):
                            return True
            return False

        return find_first_sec_num()
