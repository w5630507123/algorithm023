class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 1: return t if t in s else ""
        m, n = len(s), len(t)
        # count代表需要元素的总个数，dic代表每个元素分别还需要的个数
        count, dic = n, {}
        for c in t: dic[c] = dic.get(c, 0) + 1
        num, res = m + 1, ""
        i, j = 0, 0

        while j < m:
            if s[j] in dic:
                dic[s[j]] -= 1
                if dic[s[j]] >= 0:
                    count -= 1
            while count == 0:
                if j - i + 1 < num:
                    num = j - i + 1
                    res = s[i:j + 1]
                if s[i] in dic:
                    dic[s[i]] += 1
                    if dic[s[i]] > 0:
                        count += 1
                i += 1
            j += 1
        return res