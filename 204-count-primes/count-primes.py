class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0

        prime = [True] * n
        prime[0] = prime[1] = False

        p = 2

        while p * p < n:
            if prime[p]:
                prime[p * p:n:p] = [False] * (((n - 1 - p * p) // p) + 1)
            p += 1

        return sum(prime)