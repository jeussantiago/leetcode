class Solution:
    def confusingNumber(self, n: int) -> bool:
        valid = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'}

        n = str(n)
        s = ""
        for i in range(len(n) - 1, -1, -1):
            # print(n[i])
            if n[i] not in valid:
                return False

            s += valid[n[i]]

        return int(n) != int(s)
