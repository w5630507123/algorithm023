class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))#因为set是无序的，所以最后用sorted排序
        return len(nums[:])