class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        one_number,two_number = 1,2
        final_number = 0
        for i in range(2,n):#斐波那契数列
            final_number = one_number + two_number
            one_number,two_number = two_number,final_number
        return final_number