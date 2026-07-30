class Solution:
    def maxProduct(self, n):
        largest = 0
        second = 0

        while n:
            n, digit = divmod(n, 10)

            if digit >= largest:
                second = largest
                largest = digit
            elif digit > second:
                second = digit

        return largest * second