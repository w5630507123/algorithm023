class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        while True:#移除0的个数等于列表的长度差，最后在列表末尾添加
            try:
                nums.remove(0)
            except:
                break
        nums[::] = nums + [0]*(l-len(nums))