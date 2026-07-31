class Solution(object):
    def arrangeCoins(self, n):
        left = 0 
        right = n
        rows = 0
        while left<=right:
            mid = (left+right)//2
            coins_needed=mid*(mid+1)//2
            if coins_needed <= n:
                rows = mid
                left=mid+1
            else :
                right=mid-1
        return rows 