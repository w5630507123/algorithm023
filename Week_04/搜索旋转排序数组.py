class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start,end = 0,len(nums)-1
        while start <= end:
            mid = (end - start)//2 + start
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target and target<=nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1