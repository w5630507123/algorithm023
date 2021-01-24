使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方：
思路：①首先保持二分法的思路，因为数组还是相对有序，只是分为了两部分有序
②细微调整，可以理解为二分法的变种。

假如我们设目标查找目标数字是target，

if not nums:

    return -1
    
start,end = 0,len(nums)-1 #和二分查找一样的思路，定义两个指针

while start <= end:

    mid = (end - start)//2 + start #防止越界，虽然Python3理论上不会越界，但保持良好的习惯，其他语言可能会越界
    
    if nums[mid] == target: #如果等于，则找到，直接return
    
        return mid
        
    if nums[0] <= nums[mid]: #如果中间数字大于第一个数字，则说明中间数字在前半部分。
    
        if nums[0] <= target and target < nums[mid]:#如果target属于这个部分，则在这个部分二分查找，反之则在另外一个部分
        
            end = mid - 1
            
        else:
        
            start = mid + 1
            
    else:
    
        if nums[mid] < target and target<=nums[end]:
        
            start = mid + 1
            
        else:
        
            end = mid - 1
            
return -1
