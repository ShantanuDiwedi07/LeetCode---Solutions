class Solution(object):
    def lexGreaterPermutation(self, s, target):
        n = len(s)
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Try to match target from left to right
        i = 0

        while i < n and count[ord(target[i]) - ord('a')] > 0:
            count[ord(target[i]) - ord('a')] -= 1
            i += 1

        while True:

            # Try to put a character greater than target[i]
            if i < n:
                cur = ord(target[i]) - ord('a')

                for c in range(cur + 1, 26):
                    if count[c] > 0:

                        ans = target[:i]
                        ans += chr(ord('a') + c)

                        count[c] -= 1

                        # Put remaining characters in sorted order
                        for x in range(26):
                            ans += chr(ord('a') + x) * count[x]

                        return ans

            # Couldn't make current position greater
            # Backtrack
            if i == 0:
                return ""

            i -= 1
            count[ord(target[i]) - ord('a')] += 1