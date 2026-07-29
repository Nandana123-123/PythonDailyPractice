import collections

class Solution(object):
    def __init__(self):
        self.MAX = 10**6 + 1

    def smallestPalindrome(self, s, k):
        count = collections.Counter(s)

        odd = 0
        for v in count.values():
            if v % 2:
                odd += 1

        if odd > 1:
            return ""

        half = [0] * 26
        mid = ""

        for c in count:
            half[ord(c) - ord('a')] = count[c] // 2
            if count[c] % 2:
                mid = c

        if k > self.countWays(half):
            return ""

        left = []
        m = sum(half)

        for _ in range(m):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = self.countWays(half)

                if ways >= k:
                    left.append(chr(i + ord('a')))
                    break
                else:
                    k -= ways
                    half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]

    def countWays(self, cnt):
        total = sum(cnt)
        ans = 1

        for x in cnt:
            ans *= self.nCr(total, x)
            if ans >= self.MAX:
                return self.MAX
            total -= x

        return ans

    def nCr(self, n, r):
        if r < 0 or r > n:
            return 0

        r = min(r, n - r)
        ans = 1

        for i in range(1, r + 1):
            ans = ans * (n - i + 1) // i
            if ans >= self.MAX:
                return self.MAX

        return ans


# ---------------- MAIN ----------------
obj = Solution()

# Test Cases
print(obj.smallestPalindrome("abba", 1))   # abba
print(obj.smallestPalindrome("abba", 2))   # baab
print(obj.smallestPalindrome("aa", 2))     # ""
print(obj.smallestPalindrome("racecar", 1))