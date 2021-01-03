class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return None
        nums_dict = {} #设置一个字典
        for index in range(len(nums)):#遍历数组
            if (target - nums[index]) not in nums_dict:#实际是找数组中是否有target - nums[index]，如果使用字典则很快
                nums_dict[nums[index]] = index
            else:
                return [nums_dict[target - nums[index]],index]
        return None