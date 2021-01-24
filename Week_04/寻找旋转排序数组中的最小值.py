class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return min(nums)
        start,end = 0,len(nums)-1
        while start <= end:
            mid = (end - start)//2 + start
            if nums[mid]<nums[mid-1] and nums[mid] < nums[mid+1]:
                return nums[mid]
            elif nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] > nums[mid-1] and nums[mid] < nums[mid+1] and nums[mid] > nums[0] and nums[mid] > nums[-1]:
                start = mid + 1
            else:
            ##elif nums[mid] > nums[mid-1] and nums[mid] < nums[mid+1] and nums[mid] < nums[-1] and nums[mid] < nums[0]:
                end = mid -1
        return nums[start]