class Solution:
    def numberToWords(self, num: int) -> str:
        # Time: O(n)
        # Space: O(1)

        def words1to19(idx):
            one_to_nineteen = [
                '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
                'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
                'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
            ]
            return one_to_nineteen[idx]

        def words20to90(idx):
            tens = ['', '', 'Twenty', 'Thirty', 'Forty',
                    'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
            return tens[idx]

        def scales(idx):
            hundreds = ['', 'Thousand', 'Million', 'Billion']
            return hundreds[idx]

        def convert(num):
            if num == 0:
                return ""
            elif num < 20:
                return words1to19(num) + " "
            elif num < 100:
                return words20to90(num // 10) + " " + convert(num % 10)
            else:
                return words1to19(num // 100) + " Hundred " + convert(num % 100)

        if num == 0:
            return "Zero"

        res = ""
        scaleIndex = 0
        while num > 0:
            if num % 1000:
                res = convert(num % 1000) + scales(scaleIndex) + " " + res
            num //= 1000
            scaleIndex += 1

        return res.strip()
