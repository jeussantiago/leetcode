class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        '''
        Time: O(n)
        Space: O(1)
        '''
        def isIPV4(query):
            if len(query) != 4:
                return False

            for sub in query:
                if len(sub) < 1:
                    return False

                for c in sub:
                    if not c.isdigit():
                        return False

                int_sub = int(sub)
                if int_sub > 255:
                    return False

                if str(int_sub) != sub:
                    return False

            return True

        def isIPV6(query):
            # 0-9, a-f
            validHexdecimalValues = '0123456789abcdefABCDEF'
            if len(query) != 8:
                return False

            for sub in query:
                if len(sub) < 1 or len(sub) > 4:
                    return False
                for c in sub:
                    if not c.isdigit() and c not in validHexdecimalValues:
                        return False

            return True

        possibleIPV4 = queryIP.split('.')
        possibleIPV6 = queryIP.split(':')

        isQueryIPV4 = isIPV4(possibleIPV4)
        isQueryIPV6 = isIPV6(possibleIPV6)

        if isQueryIPV4:
            return "IPv4"
        elif isQueryIPV6:
            return "IPv6"
        else:
            return "Neither"
