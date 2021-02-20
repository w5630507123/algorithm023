class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        number_a,number_b = 1,2
        for i in range(3,n+1):
            number_c = number_a + number_b
            number_a = number_b
            number_b = number_c
        return number_c