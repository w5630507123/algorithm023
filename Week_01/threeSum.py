class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        positive = {}#算法思路，设置两个字典分别存放正数和负数，然后统计0的个数，并分情况讨论
        Negative = {}
        zero = 0
        res = []
        if len(nums)<=2:
            return []
        #分为正整数，负整数，和零的个数
        for num in nums:
            if num > 0:
                if num in positive:
                    positive[num] += 1
                else:
                    positive[num] = 1
            elif num < 0:
                if num in Negative:
                    Negative[num] += 1
                else:
                    Negative[num] = 1
            else:
                zero+=1
        #如果零个数大于3 则添加【0，0，0】
        if zero >= 3:
            res.append([0,0,0])
        #一个0一正一负的情况
        if zero > 0:
            for num in positive:
                if (-num) in Negative:
                    res.append([-num,0,num])
        #两正一负且两正相同
        for num in positive:
            if (-2*num) in Negative and positive[num]>=2:
                res.append([(-2*num),num,num])
        #两负一正且两负相同
        for num in Negative:
            if (-2*num) in positive and Negative[num]>=2:
                res.append([num,num,(-2*num)])
        #剩余的情况
        positive_list = list(positive.keys())
        for index_1 in range(len(positive_list)-1):
            num_one = positive_list[index_1]
            for num_two in positive_list[index_1+1:]:
                if -(num_one+num_two) in Negative:
                    res.append([-(num_one+num_two),num_one,num_two])
        Negative_list = list(Negative.keys())
        for index_1 in range(len(Negative_list)-1):
            num_one = Negative_list[index_1]
            for num_two in Negative_list[index_1+1:]:
                if -(num_one+num_two) in positive:
                    res.append([num_one,num_two,-(num_one+num_two)])
        return res