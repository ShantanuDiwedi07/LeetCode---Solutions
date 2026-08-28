class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        n = len(s)

        # Count characters
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one odd frequency
        odd = 0
        middle = ""

        for i in range(26):
            if count[i] % 2:
                odd += 1
                middle = chr(i + ord('a'))

        if odd > 1:
            return ""

        # We only need to construct the left half
        half = [count[i] // 2 for i in range(26)]
        left_len = n // 2

        def make_palindrome(left):
            left = "".join(left)
            return left + middle + left[::-1]

        # Greedily construct the left half
        left = []

        for _ in range(left_len):

            for c in range(26):

                if half[c] == 0:
                    continue

                # Try this character
                half[c] -= 1
                left.append(chr(c + ord('a')))

                # Make the largest possible completion
                remaining = []

                for x in range(25, -1, -1):
                    remaining.append(chr(x + ord('a')) * half[x])

                candidate_left = "".join(left) + "".join(remaining)
                candidate = make_palindrome(candidate_left)

                # If even the largest completion is not greater,
                # this character cannot work.
                if candidate > target:
                    break

                # Undo
                left.pop()
                half[c] += 1

            else:
                return ""

        answer = make_palindrome(left)

        if answer > target:
            return answer

        return ""
        