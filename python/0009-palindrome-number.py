#SIMPLE SOLUTION
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

#SOLUTION WITHOUT TURNING INT TO STRING
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x > 0 and not x%10): #any negative number or any number ending in a zero cannot be a palindrome
            return False
        temp = x
        newX = 0
        while temp > 0: #instead of looking checking the entire number, we can look up to a certain, halfway point where the new value is greater than the original value
            remainingNum = temp % 10 #get mod/remaining value of of number
            temp = (temp - remainingNum) // 10 #subtract remaining value from x value and get the floor of it to remove zero place
            newX = (newX * 10) + remainingNum #add value to new X but first shift placement of current numbers

            # print(remainingNum, temp, newX)
        if newX == x:
            return True
        return False


#SOLUTION WITH TURNING INTO TO STRING
class Solution:
    def isPalindrome(self, x: int) -> bool:

        numStr = str(x)
        i = 0
        while i < len(numStr)/2:
            if numStr[i] != numStr[len(numStr)-1-i]:
                return False
            i += 1

        num = str(x)
        reverse = num[::-1]
        if num == reverse:
            return True
        return False
