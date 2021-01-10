class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        思路同上，在Python中，这里涉及到3个知识点：
        1. 使用内置的 defaultdict 字典设置默认值；
        2. 内置的 ord 函数，计算ASCII值（等于chr）或Unicode值(等于unichr)；
        3. 列表不可哈希，不能作为字典的键，因此这里转为元组；
        """
        str_dict = collections.defaultdict(list)
        for s in strs:
          s_key = [0] * 26
          for c in s:
            s_key[ord(c)-ord('a')] += 1
          str_dict[tuple(s_key)].append(s)
        return list(str_dict.values())
