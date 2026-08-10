class Solution ():
    def isPalindrome(self,n): 
        num = str(n)
        num2 = num[::-1]
        if num==num2 :
            return True
        else :
            return False