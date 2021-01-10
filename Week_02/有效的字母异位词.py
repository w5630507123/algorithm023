class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #主要思路，建立两个字典，分别存放每个字符串中字母出现次数。最后判断两个字典是否相等
        if len(s)!=len(t):
            return False
        dict_s = {}
        dict_t = {}
        for i in s:
            if i in dict_s:
                dict_s[i] += 1
            else:
                dict_s[i] = 1
        for j in t:
            if j not in dict_t:
                dict_t[j] = 1
            else:
                dict_t[j] += 1
        if dict_s == dict_t:
            return True
        return False
        #还有一个思路是就使用一个字典，然后首先建立S的字母出现次数字典，然后遍历t，如果字典里有这个字符就减一，如果没有或者计算结果小于0，则return False
        #因为有判断两字符串长度是否相等的判定，如果相等，则最后如果遍历完没返回则直接return True