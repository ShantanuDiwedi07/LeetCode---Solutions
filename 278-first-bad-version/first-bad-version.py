class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n 
        First_bad=n
        while left <= right :
            mid = (left+right)//2
            if isBadVersion(mid):
                First_bad = mid
                right = mid-1
            else :
                left = mid +1
        return First_bad