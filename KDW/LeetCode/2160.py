'''
Author    : Dongwoo Kang
Date      : 2024.08.10(Sat)
Runtime   : 36ms
Memory    : 16.52MB
Algorithm : Permutations
'''
from itertools import permutations
class Solution:
    def minimumSum(self, num: int) -> int:
        nums = [int(i) for i in str(num)] # 2923 => [2, 9, 2, 3] 
        min_sum = float('inf')
        for per in permutations(nums): # 숫자들의 조합
            for i in range(1, len(per)):
                num1 = int(''.join(map(str, per[:i]))) # 2
                num2 = int(''.join(map(str, per[i:]))) # 923
                current_sum = num1 + num2
                if current_sum < min_sum: # 가장 작은 수를 반환
                    min_sum = current_sum
        return min_sum

# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/