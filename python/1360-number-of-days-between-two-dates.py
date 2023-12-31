class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = datetime.datetime.strptime(date1, '%Y-%m-%d').date()
        d2 = datetime.datetime.strptime(date2, '%Y-%m-%d').date()
        return abs((d1 - d2).days)
