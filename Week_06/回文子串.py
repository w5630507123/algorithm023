class Solution:
    def countSubstrings(self, s: str) -> int:
        l,res = len(s),0
        dp = [[0]*l for _ in range(l) ]
        for j in range(l): # 遍历外层是列遍历
            for i in range(0,j+1):
                if i==j:   # 对角线元素
                    dp[i][j] = 1
                    res +=1
                elif j-i==1 and s[i]==s[j]: # 相邻元素
                    dp[i][j] = 1
                    res +=1
                elif  s[i]==s[j] and dp[i+1][j-1]:  # 非相邻元素
                    dp[i][j] = 1
                    res +=1
        return res