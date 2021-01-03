class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for index in range(len(digits)-1,-1,-1):
            if digits[index] != 9: #尾数小于9，不用进位的情况
                digits[index] += 1
                break
            elif index==0 and digits[index]==9: #情况为999的类似情况
                digits[index] = 0
                digits.insert(0,1)
                break
            else: #其他类似1239 1399等情况
                digits[index] = 0
        return digits