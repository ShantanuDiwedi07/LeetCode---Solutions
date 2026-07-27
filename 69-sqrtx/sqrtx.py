class Solution(object):
    def mySqrt(self, x):
        left = 0
        right = x
        ans = 1
        while left<=right: 
            mid = (left+right)//2
            if mid*mid == x :
                ans= mid
                return ans
            elif mid*mid < x:
                ans= mid
                left=mid+1
            else :
                right = mid-1
        return ans