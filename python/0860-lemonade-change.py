class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = collections.defaultdict(int)
        for bill in bills:
            money[bill] += 1

            if bill == 10:
                if money[5] == 0:
                    return False
                money[5] -= 1

            elif bill == 20:
                if money[10] == 0:
                    if money[5] >= 2:
                        money[5] -= 2
                    else:
                        return False
                else:
                    money[10] -= 1

                if money[5] == 0:
                    return False
                money[5] -= 1

        return True
