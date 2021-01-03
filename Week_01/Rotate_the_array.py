class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)#判断k是否大于列表长度，若大于，取模
        if k > l:
            k = k % l
        nums[::] = nums[-k:] + nums[:-k]
        return nums