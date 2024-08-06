'''
Author    : Dongwoo Kang
Date      : 2024.07.31(Wed)
Runtime   : 278528 KB
Memory    : 37 ms
Algorithm : Binary Search
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        radix = 5
        ans = 0

        while n >= radix and radix < 10000:
            ans += n // radix
            radix *= 5
        return ans
    
