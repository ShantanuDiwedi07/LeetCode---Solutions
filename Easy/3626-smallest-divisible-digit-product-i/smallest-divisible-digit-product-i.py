class Solution(object):
    def smallestNumber(self, n, t):
        def product(x):
            p = 1
            while x > 0:
                p *= x % 10
                x //= 10
            return p

        x = n

        while True:
            prod = product(x)

            if prod % t == 0:
                return x

            x += 1