class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        lenS = len(s)
        dp = [0] * lenS
        dp[0] = 0 if s[0] == '0' else 1
        for i in range(1, lenS):
            t1 = (dp[i - 1] if s[i] != '0' else 0)
            t2 = (dp[i - 2] if i - 2 >= 0 else 0)
            t3 = int(s[i - 1: i + 1]) <= 26 and s[i - 1: i + 1][0] != '0'
            dp[i] = t1 + (t2 if t3 else 0)
            if i - 2 < 0 and t3:
                dp[i] += 1
        return dp[-1]